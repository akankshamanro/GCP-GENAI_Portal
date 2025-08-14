from flask import Blueprint, render_template, jsonify
import aiohttp
import asyncio
import json

views = Blueprint('views', __name__)

CONFIG_FILE = "config.json"

async def check_health(session, service_url):
    try:
        async with session.get(service_url) as response:
            if response.status == 200:
                return {"url": service_url, "status": "healthy"}
            else:
                return {"url": service_url, "status": "unhealthy", "status_code": response.status}
    except aiohttp.ClientError as e:
        return {"url": service_url, "status": "unhealthy", "error": str(e)}

@views.route("/health-check")
async def health_check():
    with open(CONFIG_FILE, "r") as config_file:
        config = json.load(config_file)
    services = config.get("services", [])
    
    async with aiohttp.ClientSession() as session:
        tasks = [check_health(session, service_url) for service_url in services]
        results = await asyncio.gather(*tasks)
    
    return jsonify(results)

@views.route("/")
async def index():
    with open(CONFIG_FILE, "r") as config_file:
        config = json.load(config_file)
    services = config.get("services", [])
    
    async with aiohttp.ClientSession() as session:
        tasks = [check_health(session, service_url) for service_url in services]
        results = await asyncio.gather(*tasks)
    
    return render_template("health.html", results=results)
