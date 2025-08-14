import gradio as gr
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://seorevolution-gpt4.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = "990eef0d10e44286989c7e8745e8c245"

def content_extraction(reference1,reference2,reference3,choice):
    

    if "Topic" in choice :
        system='''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        '''

        user_prompt = f'Extract top 5 Topic from these three given articles/blog post for SEO : {reference1},{reference2},{reference3}. '
        response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        result=response.choices[0].message['content']  

        return result
    
    

  
def generate_keywords(reference1,reference2,reference3,Topic,Keyword):
    results1=[]

    if "Similar Keyword" in Keyword:
        system = ''' 
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate Keyword on given topic only.
        '''

        user_prompt=f'''

        Give me top five exact matched keywords for this topic : {Topic} that are present in these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
        
        '''  
        response_similar = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
        results1.append ("Similar Keywords:\n"+  response_similar.choices[0].message['content']  )
    

    if "Long Tail Keyword" in Keyword:
        system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate Keyword on given topic only.
        '''

        user_prompt=f'''

        Extract top five long tail keywords for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
        '''  
        response_long_tail = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
        results1.append ("Long Tail Keywords :\n"+  response_long_tail.choices[0].message['content']  )
    

    if "Short tail Keyword" in Keyword:
        system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate Keyword on given topic only.
        '''

        user_prompt=f'''

        Extract top five Short Tail keywords for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}.
        '''  
        response_short_tail = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
        results1.append ("Short Tail Keywords :\n"+  response_short_tail.choices[0].message['content']  )
    

    if "Semantically Related" in Keyword:
        system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.

        Instructions :
        You have to generate Keyword on given topic only.
        '''

        user_prompt=f'''

        Extract top five Semantically keywords for this topic : {Topic} from these three given article/blog post for SEO: {reference1},{reference2},{reference3}. 
        '''  
        response_semantically = openai.ChatCompletion.create(  
        engine="AIKillsSEO",  # Use an actual engine  
        messages=[{"role":"system","content":system},
        {"role":"user","content":user_prompt}],  
        temperature=0.8,  
        max_tokens=3000,  
        top_p=1,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=["#", ";"]  
        )
        results1.append ("Semantically Related Keywords :\n"+  response_semantically.choices[0].message['content']  )

    return "\n\n".join(results1)




# Weekly Tech Blog

t_blog1 ='''
Floating solar platforms are green energy’s next big thing
Solar farms at sea may be clean energy’s next breakthrough.

Headshot of Digitally Cognizant author Tech to Watch
Tech to Watch Blog

Visit our Sustainability & Resilience webpage
In the news
Will the cruise to net zero take the world over the bounding main? Some believe it will; right now, in the Yellow Sea, a key experiment is underway in which arrays of floating solar panels are torture-tested to see how they stand up against the elements. When and if such panels can be sufficiently ruggedized, experts believe, offshore solar will become a significant piece of the renewable energy puzzle.

The trial is being performed by State Power Investment Corp., a major Chinese renewable-power outfit, and Norwegian firm Ocean Sun AS. The idea is to exploit the earth’s 139 million square miles (361 million square kilometers) of ocean to help land-constrained regions transition away from fossil fuels. Interest is especially high in parts of Europe, Asia and Africa, where it’s impractical or impossible to devote enough land to solar panels—because the acreage simply doesn’t exist or is too rugged.

The potential scale of successful offshore solar is awe-inspiring. Shandong alone, China’s second most populous province, plans to add 42 gigawatts of floating panels eventually—more than the current capacity in all of Norway. Japan, the Netherlands and Malaysia, among others, are also testing the technology.

And those tests are not slam-dunks. Waves, rain and continuous salt spray place enormous demands on the panels. Moreover, their effects on the marine environment are largely unknown. Another test, this one by a Belgian consortium dubbed SeaVolt, is just beginning, with the goal of learning more about the impact of these factors on floating solar platforms.

If these challenges can be overcome, offshore solar’s advantages (including the built-in cooling that increases panels’ performance and the potential for combination with wind power) make for nearly unlimited potential.

The Cognizant take
According to Jan Konietzko, Manager, Sustainability Advisory at Cognizant, the opportunities presented by offshore solar arrays are compelling for one obvious reason: surface area. “It could be a major factor anywhere you have space constraints,” he says, noting the Netherlands as one example.

But the challenges are as clear as the potential. Consider the North Atlantic—it’s about as harsh an environment for high-tech equipment as you can imagine, no matter how well that gear is ruggedized. “Salt, wind, waves,” Konietzko says. “There are just so many problems.” He notes that even land-installed solar panels face more maintainability and reliability issues than most people realize; some number of them crack during mere transport.

However, the same digital solutions that help utilities maintain field equipment could help with offshore solar. Visual inspection via drones and wear data gathered through sensors and intelligently analyzed are two examples noted by Konietzko.

The other major holdup that warrants investigation is the impact large-scale solar arrays may have on ocean life. At present, the impact is simply unknown, though experiments to gauge it are ongoing. It certainly stands to reason that reducing available sunlight will affect undersea life.

“We need to, and can, better understand the ocean through data,” Konietzko notes. He points to a collaboration between Cognizant and Tidal that aims to do just that. Tidal offers data-driven insights to companies and industries that rely on oceans. Monitoring data could be used to “understand the impact that solar PV panels on the water surface have on the life underneath,” he says.

With renewable energy becoming a more and more important factor in sustainability, it certainly makes sense to leverage as much of the earth’s surface as is feasible.

Digital Business & Technology , Tech to Watch  sustainability , solar panels , Solar energy , green energy
'''


t_blog2='''
What the fusion energy breakthrough really means
While the benefits of fusion ignition won’t be seen for decades, they will be life-changing from a sustainability standpoint.

Headshot of Digitally Cognizant author Tech to Watch
Tech to Watch Blog

Visit our Sustainability Services webpage
In the news
It was hard to miss the recent news that researchers at Lawrence Livermore National Laboratory, a federal facility in California, achieved one of energy science’s long-sought-after breakthroughs: a fusion reaction that produced a net energy gain.

Since March 2020, most would agree that bad news has outweighed good (pandemic, war, inflation … need we go on?), so the optimism bordering on glee demonstrated by political types is understandable. US President Joe Biden, perhaps emulating John F. Kennedy’s famous call for a moon landing within a decade, said he wants fusion power by 2032.

A brief explainer: The type of nuclear energy used today is derived through the splitting of atoms—fission. By contrast, fusion (which is the energy source of stars), combines, or fuses, atoms. Researchers have been chasing a net-energy-gain fusion reaction for more than half a century because it “creates less radioactive material than fission and has a nearly unlimited fuel supply,” as this post notes.

Is it feasible to commercialize fusion within a decade? Spoiler alert: no. Nevertheless, the potential energy and sustainability benefits of the breakthrough boggle the mind.

The Cognizant take
One problem with the Next Big Thing—any Next Big Thing—is that it makes people feel as if a problem has been solved. Business leaders must avoid this trap where fusion is concerned. The mere reality of a net-energy-gain reaction is not an end, but a beginning. It’s another arrow in the sustainability quiver, which we cover extensively here.

Companies that have only recently begun focusing on reducing the carbon footprint of their products, processes and facilities must continue doing so, not only to gain competitive advantage but also to ensure resilience.

There are pragmatic reasons, as well. Many sources of greenhouse gas emissions won’t be impacted by fusion ignition because they aren’t related to electricity: fertilizers, methane from cattle in meat and dairy production, the burning of fossil fuels in transportation and manufacturing, and on and on. So, while the world needs 100% clean electricity, it also needs to electrify more energy needs; otherwise, these other factors will continue increasing CO2 equivalent levels in the atmosphere.

Additionally, most estimates point to fusion being commercially available in the second half of this century (some private companies are more optimistic, as you’d expect). What that means is we will need to have achieved net zero before fusion becomes commercially available. So, while fusion is highly promising in terms of making sustainable economic prosperity possible in a net zero world, it’s unlikely to help us get to net zero in a prosperous economy.

Its important to note that the optimism around the fusion breakthrough is warranted. Already, multiple enterprises are working to make fusion power a reality. If you are optimistic about humankind’s ability to safely use this energy, as we are, it’s no exaggeration to draw comparisons to the ability to store and harness electricity. Imagine having available the most efficient and environmentally safe power in the universe—the power of the sun, quite literally. It’s more than another tech breakthrough; it’s a giant step forward for humans and for the earth.

Digital Business & Technology , Tech to Watch  sustainability , Fusion energy , fusion ignition

'''

t_blog3=f'''
Look to gen AI to rev up the metaverse
As gen AI become more pervasive, it will help create data-rich immersive experiences on metaverse-like platforms.

Headshot of Digitally Cognizant author Tech to Watch
Tech to Watch Blog

Visit our generative AI webpage
In the news
With today’s compressed news cycle, it can be difficult to keep track of what’s hot and what’s decidedly not. This is the case in politics, entertainment and sports—so why shouldn’t it be true in the technology sector as well?

The metaverse is Exhibit A. Facebook kicked off a hype cycle in late 2021 when the company renamed itself Meta. The ensuing arc began with “One of the hottest trends in the tech world,” and ended with “The hype bubble has popped” almost exactly a year later.

Apple’s Vision Pro briefly spiked metaverse interest, but you could be forgiven for thinking the technology had, like the band in the mockumentary This Is Spinal Tap, relocated to the Where Are They Now file …

… and that generative artificial intelligence (gen AI) had driven the moving van. For it was gen AI, and its most familiar application OpenAI’s ChatGPT, that pushed the metaverse off the front page. Seemingly overnight, the world shifted its interest from wearing metaverse headsets to never again writing original reports, software code or music.

But when you get past that rapid-fire news cycle and the short attention spans it has engendered, the relationship between the metaverse and gen AI is far more complex. “Generative AI,” as one clear-headed report notes, “can play a significant role in empowering interactions and development on the metaverse.”

The Cognizant take
For starters, says Duncan Roberts, thought leader and futurist at Cognizant Research, creative applications of generative AI will help fill the enormous need for content as developers create virtual worlds populated by three-dimensional assets. Typically, 3D modeling is labor-intensive—but gen AI can create contents from text descriptions.

That’s a powerful shortcut. “Generative AI will eventually be able to create any environment we want at the drop of a hat—the Star Trek holodeck, if you like,” Roberts says. We’re still a long way off from that, he concedes, “but I can definitely see a path to it.”

Already, one application of gen AI is to make bots—such as those used in training, customer service and, yes, the metaverse—far more human-like. Roberts expects such use cases to evolve quickly. But perhaps the most intriguing connection between gen AI and the metaverse is the relative ease with which the former bolsters the latter. “Some have estimated that a triumph of creativity like the film Avatar: The Way of Water, which was years in the making, could be done in months with generative AI,” he says.

Roberts wrote recently about peeling back technology hype, as well as the errors and false expectations that come with it, by breaking technologies into their component parts. “Too often, we talk about technology just for its own sake,” he writes. “However, the first question anyone should ask after understanding the basics of a new technology is not how to use it, but what they are trying to achieve.”

Viewed this way, the metaverse and generative AI are not competitors for consumer mindshare, but rather complementary technologies that can be used to better the organization—and more.

Digital Business & Technology , Tech to Watch  metaverse , gen AI , generative AI

'''





# Informative/Descriptive Blog

d_blog1='''
Tender and deal management: The journey to excellence
For life sciences companies, improved tender and deal (non-tenders) management is a must – but there’s more to it than buying software.

Few processes impact a life sciences organization’s bottom line as much as tender and deal management. Tenders, the bidding processes that public hospitals must use to procure goods and services, represent up 70% to 85% of revenue for medical technology companies and 25% to 40% for pharmaceutical companies. They are complex, rigid processes that require rapid, seamless collaboration to produce bids that meet the bidder’s revenue and profit targets as well as customer- and often country-specific requirements. Optimizing the management of tenders—and deals, their private-sector contracting counterpart often used by buying groups in the US, Germany, Netherlands and Japan—represents a major opportunity.

Despite its importance, tender and deal management often relies on manual, disjointed processes using spreadsheets and emails. Those responding to tenders and deals lack a single repository of reliable information as well as standard systems, price governance, audits, and business approach.


On average, six departments within MedTech devote 200 to 500 hours to each tender, with salespeople spending up to 50% of their time on tender-related administrative work.

This disjointed approach often leads to a lack of visibility, which may leave organizations only 35 days to prepare and submit bids. Cumbersome information sharing, meanwhile, makes it difficult to decide which opportunities to compete for, and which prices and other terms to offer in bids. All this means excess cost and lost opportunities when prices are set too high, or lost revenue and profits when bids are too low.

Given all this, achieving tender and deal excellence is an opportunity to increase revenues at pharmaceutical and medical technology companies 3% to 5%, boost profits up to 3%, and reduce tender- and deal-related costs up to 25%, all while limiting the risk of non-compliance penalties.

So what must life sciences do to improve their tender and deal management?

Some have started to reevaluate their strategies. Often, that reevaluation begins and ends with an all-in-one tender and deal management technology platform integrated with other core business systems. We have found, however, that achieving excellence also requires optimizing people’s roles and skills, as well as business processes, across the tender and deal management lifecycle. Here’s what that journey entails at each stage:
Discovery

Increased visibility into current and upcoming (anticipated) opportunities allows the entire organization to plan better—gathering the information, systems and processes required to properly bid for existing tenders and to shape tenders before they are published. By identifying opportunities 12 to 18 months in advance, the sales team and account managers will have ample time to prepare a business plan and lobby to become the preferred supplier, all with the help of a guided sales workflow with predefined tasks and milestones. This also provides time to shape the tender or deal by encouraging the issuer to include requirements and weighted award criteria that will help your organization win. This step is critical; many experts estimate that nearly half the work required to win a tender occurs before it is published.

Collecting and analyzing data can also help life sciences companies make informed decisions about which opportunities are worth spending the time, money and effort to pursue. Once the business connects to multiple local online publication platforms, smart search with AI can be used to automatically find information about upcoming tenders and deals. Machine learning (ML) can automatically make recommendations, based on specified business criteria, regarding whether to bid on each lot of the published tender. Once qualified, the publication details can be imported into the tender and deal management tool, automatically creating the bid proposal structure for submission.

Discovery also requires a dedicated bid team with clear roles and responsibilities and the skills to carry them out. Workflows should define what data various collaborators, such as sales, finance, demand planning, and legal and compliance require.

Execution

Execution comprises all the work required to create and submit a winning bid for a tender or deal—and, if it is won, fulfilling the terms of the contract and maximizing the resulting revenue and profit.

This includes managing and tracking opportunities and proposals in the bid pipeline and ensuring proposals are submitted before the deadline. Tender and deal managers must update the business case first prepared during the discovery phase (or develop a new one if details of the published tender dictate). This requires analyzing the requirements as well as past tender performance, previous winning prices, strategic goals of the business, and likely bids from competitors. In the process, tender and deal managers must collaborate with functions such as sales, finance, demand planning, finance and legal to build a winning proposition while adhering to company policies.

In this phase, AI can help estimate both optimum pricing and win probability. Automated scorecards can simulate alternatives, taking into account pricing and qualitative award criteria scoring, and ultimately arrive at an optimal winning bid scenario that is still profitable. The pricing and legal functions must be updated to ensure compliance with corporate policies.

If the bid is won, the tender or deal manager needs to update the system and capture outcome details. To ensure that required products are available at the proper time and place, the manager must update the supply chain, as well as corporate planning, finance and sales to ensure proper budgeting, forecasting and invoicing for the contract period.

Governance

Governance is the process of ensuring the company fulfills the requirements of bids it has won, but also of improving the performance of the entire tender and deal management process. This is accomplished by replicating what worked well and making improvements where needed.

Another essential function is measuring and optimizing metrics such as volume delivered vs. volume called for in the contract; profitability; and penalty avoidance for non-delivery. The account manager must be kept informed of the contract performance and any possible extensions. They should also both proactively advocate for such extensions to maximize revenue and delay the publication of a new tender (which would require new competition). While monitoring contract performance, the account manager should focus on ensuring pull-through sales under the current contract, while planning for and shaping future opportunities.

Reporting on various metrics and decision outliers, as well as tracking key performance indicators (KPIs) such as win and conversion rates and supply fulfillment rates, helps all players understand what needs to be improved.
Replacing siloed, manual tender and deal management systems with a single technology solution speeds a life sciences company’s journey to excellence.


It can automate and standardize common processes, while giving all stakeholders a unified view of data, processes and the status of tenders and deals. Rather than building such a tool in-house, we recommend choosing an off-the-shelf solution for the fastest, most efficient rollout, as several solutions have matured considerably.

While some may believe the deployment and integration of such a global tool is too long and expensive to be feasible, we have implemented several solutions with multiple life sciences companies in as little as 12 months across more than 80 markets around the world. Because excellence in tender and deal management involves new tools, processes and skills, change management is required to assure adoption of the new platform through training and education about its benefits.

Assess your readiness
In our experience, many life sciences companies believe their tender and deal management capabilities are more mature than they really are. In some cases, the level of excellence in one geography or business unit is not matched by the entire organization.

Rigorously assessing the right KPIs is the only way a business can properly understand its current level of excellence and where improvement is needed. The sooner life sciences organizations begin pursuing tender and deal management excellence, the sooner they will reap the rewards of increased revenues and profits with lower risks.
'''


d_blog2='''
4 ways clinical development will improve with gen AI
By changing their approach to clinical development with generative AI, life sciences companies can realize exponential revenue opportunities and offer renewed hope to patients.

When it comes to clinical development, saving time translates to saving lives, or at least improving them, through faster availability of treatments. For life sciences companies, it also translates into revenue opportunity—and a significant one at that. Some industry sources estimate that delivering new treatments to market ahead of schedule can be worth anywhere from $600,000 to $8 million per day.

The promise of speed is why generative AI is so compelling for life sciences companies. Generative AI helps automate standard development processes, find patterns, identify insights and produce relevant, meaningful content in any number of formats, all in a fraction of the time it would take for a human to do so.

We’ve identified four key areas of the clinical development lifecycle that can be accelerated and enhanced through the use of generative AI and supporting technologies. For life sciences companies that adopt gen AI, clinical development efficiency gains will be measured not in days or weeks but in months or even years—representing both an exponential revenue opportunity and renewed hope for patients.

Four ways to use gen AI in clinical development
#1: Streamline research processes using semantic search. Generative AI could fundamentally change the clinical and scientific research process. Instead of beginning with a manual keyword search and sifting through hundreds of articles across various sources, research teams could prompt a generative AI-enabled tool to rapidly search, gather and distill relevant articles or even suggest unanticipated information pathways to explore. This frees researchers to focus on analysis.

In our client engagements, we’ve seen 10X time savings when life sciences companies have applied generative AI to the research process.

Generative AI could also change how research is conducted. Because the underlying models understand intent and context, these tools can work from a mission- or goal-based prompt, as opposed to relying on traditional keyword searches.

For example, if a company is developing a cholesterol medication, a traditional process might begin with keyword searches involving different combinations of terms like "cholesterol," "clinical trial,” "efficacy," "safety," "hyperlipidemia" and "statins," ultimately uncovering disparate results across different source platforms.

However, with an AI-enabled tool, researchers could state their goal and receive contextualized reference materials to support that specific concept. “I'm designing a clinical trial for a new cholesterol medication,” a researcher might state to a generative AI tool. “Please provide an overview of the most recent studies on cholesterol medications, their efficacy and safety, and how they compare with existing treatments. Also, any insights on best practices and regulations would be valuable."

Finally, generative AI can also be used to analyze and synthesize relevant research materials and present them in a digestible way to a variety of constituents, from team members across multiple departments, to regulatory agencies, to institutional and ethical review boards. Ideally, these summaries would include a high degree of explainability regarding why those materials were selected. This further expedites the review process, which can also unlock time savings.

The value of explainability in generative AI
Explainability is the ability of the generative AI-enabled tool to document how it arrived at the conclusions presented in a given output and provide a rationale for any recommendations being proposed.

For example, when authoring a clinical trial protocol, the tool may include references to past protocols in a government database with similar trial dynamics, as well as components from successful trials.

This capability can help researchers and other team members quickly assess the output, view it within the proper context and identify the best next step in the process.


#2: Automate the authoring of clinical trial protocols to improve efficiency and access. It can take a few months to over a year to author a clinical trial protocol document. But companies that leverage generative AI and large language models (LLMs) can dramatically reduce that time, to days or even hours.

A foundational model for research can be fed and trained on thousands of clinical trial protocols available online through government and industry databases and proprietary company research data. As such, generative AI-enabled tools can quickly scan thousands of entries within a given database and identify the patterns relevant to investigational products, certain conditions, specific patient populations or other factors. If the company has its own proprietary data, the tool can also incorporate that information into the foundational research model.

As the tool identifies relevant patterns, it can design a baseline study, define the narrative, determine eligibility, draft exclusionary criteria and provide other details. The draft, or a group of draft options, can then be evaluated and refined by a human.

It’s also possible to expedite the protocol review and approval cycles because the protocol could be summarized and accompanied by an explanation. We estimate that life sciences companies can shave 50% to 60% off the time spent writing protocols, while reducing related review cycles another 10% to 20%.

50%-60% estimated reduction in clinical trial authoring times.


Life sciences companies can also use generative AI to design studies that leverage other digital capabilities or enable a non-traditional trial model, such as a decentralized, virtual or hybrid format.

For example, during the authoring phase, the foundational model or LLM could leverage valid data from wearables, sensors or other means of collecting biomarkers outside of a traditional clinical trial site or clinical setting. When they have specific information about the technologies needed to enable such a trial, companies can consider a wider range of options, which may, in turn, allow them to recruit from a larger base of participants.

In this way, generative AI isn’t just expediting the authoring process, but potentially designing a trial format that would speed recruitment, enrollment and testing.

Beyond identifying eligible trial participants, generative AI could also analyze demographic and behavioral data to suggest population segments likely to use these tools and remain engaged throughout the study.

One high-profile example of how generative AI is being used within the medical research community is AlphaFold. This AI program, developed by Google DeepMind, leverages deep learning to perform predictions of protein structures based on its string of amino acids. With this technology, what once took years of research can now be reduced to minutes.


#3: Identify areas for improvement through next-gen clinical study reports. It’s very time-consuming to analyze clinical trial data and summarize it in a way that demonstrates statistical significance, while also maintaining safety and efficacy standards. It’s also prone to error when done manually.

For years, conventional AI has been used to accelerate this compilation of data through prediction and probability. However, generative AI can reveal new connections not immediately apparent to human researchers or conventional models.

For example, traditional AI may be able to extract a key statistic, such as trial recruitment velocity. However, with generative AI, the model could explain the reason behind that number and also offer recommendations for improvement.

The additional context and recommendations could include:

They are behind schedule by 40% and need to recruit another 120 people in two months to meet the current deadline

Social media channels, like Facebook and Instagram, are the highest-performing recruitment channels

Increasing the social media promotion budget by 60% (and reducing traditional ad buys) is likely to help them meet their recruitment goals. The gen AI tool could generate content relevant to specific trial and patient populations, including messaging, visuals and tone for these promotions

Further refining the target audience for social ads could accelerate enrollment by up to 10%
One of the major value drivers of generative AI is that this information is all conveyed in an easy-to-understand format. No longer would research teams need to review several pages of Excel-based data or perform manual calculations to see how changes in the strategy may affect outcomes. Nor would they need to cross-reference data with social media plans or ad buys. Instead, the tool takes all that information and consolidates it into a clear list of recommended actions.

Yseop, an AI software company working with enterprises in highly regulated industries, developed Yseop Copilot, a secure content automation solution. Yseop Copilot leverages pre-trained LLM models for the biopharma industry to automate scientific content creation, helping medical writers across hundreds of clinical trials to significantly cut writing times.


#4: Expedite the treatment launch process. Once approval for a new therapy is secured in a primary market, a tremendous amount of work goes into launching the drug in a secondary market. This includes strategy development, market research, contracting, pharmacy benefit manager (PBM) negotiations, agency engagement, content creation and material development. As with the research and protocol writing processes, much of this activity could be automated through generative AI. And, as noted above, gen AI-enabled tools can also provide recommended actions to improve outcomes or further accelerate the process.

We estimate that companies could generate another 10X time savings, compared with traditional processes, through the use of gen AI in this area. For example, when a drug is close to gaining approval, generative AI can help commercial teams research and compile baseline strategy documents for secondary markets, taking into account any specific regulations that need to be adhered to.

In addition, generative AI-enabled tools can be used to translate existing materials, such as ads, websites, brochures or other sales materials, so that these assets reflect the local language and culture. Using the technology in this way could shed an additional year from the go-to-market timeline and dramatically reduce costs related to content creation and design across various markets.

Adopting and scaling gen AI in clinical development
While generative AI will undoubtedly play a role in the future of the life sciences industry, factors such as an uncertain regulatory landscape, coupled with the rapidly evolving nature of generative AI itself, are prompting some companies to delay investment until the course ahead is clearer.

However, those who take a strategic approach at this early juncture and build maturity will likely find themselves with a strong competitive advantage as the rest of the industry plays catchup.

With that in mind, here are six recommendations for building generative AI maturity today:
Foster a culture of AI literacy

To reap the full value of generative AI, everyone in the business needs a basic understanding of how generative AI will reshape their functional area. That learning process should begin now, through training courses that focus on the specific opportunities and benefits generative AI presents for each team, as well as its potential to disrupt some existing workflows. Ultimately, the energy and excitement of people will help improve the speed of adoption, maturity and scaling of more advanced use cases.

Build a robust partnership ecosystem

With the scarcity of generative AI expertise, companies need to build an ecosystem of partners, including relationships with academic institutions, hyper-scalers, data providers and specialty gen AI vendors to accelerate knowledge building and implementation of gen AI solutions. At the same time, it is important to work with a business transformation partner that can help the organization develop its internal capabilities over time. In the case of life sciences, it is critical to select an organization that not only understands the technology but also the industry, its challenges and regulatory landscape.

Establish governance

Ethical, responsible and safe use of generative AI is especially important for life sciences companies, which need to guard both sensitive patient data and intellectual property. As regional and industry standards develop, it is up to organizations to assess and mitigate risk and biases consistently and actively. This is another area where a trusted partner can help, assisting organizations as they develop, deploy and oversee necessary protocols to ensure the technology is being used safely and responsibly.

Experiment and learn

Now is the time to empower teams to explore use cases, experiment with the technology and run small-scale pilots to further those efforts and identify high-value opportunities to scale. To support our clients in this journey, we have developed a use case prioritization framework and other tools to help companies identify high-value use cases and evolve ideas into proofs of concept and production solutions.

Own critical expertise

It’s critical to establish a center of excellence (CoE) or other body to oversee the strategy and activity for the organization as a whole, as well as manage staff upskilling and development. This CoE should also identify best practices and develop frameworks and repeatable solution accelerators to institutionalize key capabilities.

Plan for adaptability

Because the technology is still evolving, as is the regulatory landscape, companies should take an agile approach so they can adapt their strategies as generative AI matures. In addition, companies should align audit and regulatory activity to support explainability and transparency and enable rapid adaptation if and when the landscape requires it. Designing flexible strategies and initiatives is the key to success in a high-potential but uncertain environment.
Unlocking gen AI impact in clinical development
Most of the use cases explored here are relatively straightforward, both in terms of their practicality and low barriers to deployment. They represent a low-risk, high-reward value proposition.
However, far more advanced use cases represent the next generation of this technology, such as using generative AI-enabled telehealth tools for patient companion apps. These applications, which would mimic a traditional caregiver experience and provide one-on-one patient support, present a tremendous opportunity to improve access to care, while also addressing significant shortages of healthcare professionals.

As life sciences companies experiment with generative AI, they will begin to lay the foundation needed to harness its full potential for both their own business and the people they serve.
'''


d_blog3=''' 
Navigating change: gen AI and entertainment jobs
Media & entertainment jobs will evolve, not disappear, as the technology takes hold.

Technological revolutions cost some people their jobs. They just do; there’s no sense sugarcoating it. Ask the teenage pinsetters at your local bowling alley. Ask the folks who lug pallets of IBM punch-cards from one corporate department to another. Ask your local video rental store.

But while you’re at it, talk to a 25-year-old with a burgeoning career advising YouTube content creators, and to someone who’s launched a half-dozen successful apps despite not knowing a lick of coding. Because technology creates more jobs than it eliminates— and nowhere is that truer than in the media & entertainment sector.

Generative AI will indeed reduce the industry’s need for certain types of work. But the benefits the tech brings, along with new jobs to enable those benefits, are nothing short of stunning. By automating routine tasks, it will free the creative workforce to focus on high-level tasks that require complex decision making, emotional intelligence, and artistic flair. And those creative professionals will have more time to experiment, explore, and push the boundaries of entertainment and storytelling.

Creative teams will use gen AI-generated suggestions and prototypes as starting points, sparking fresh ideas. The technology’s core strength of processing and analyzing vast amounts of data quickly will allow employees to make informed decisions more efficiently—whether optimizing crowd flow in theme parks, analyzing viewer preferences for content creation, or predicting merchandise trends.

Generative AI will also help businesses maintain consistency across various touchpoints, such as branding, customer interactions, and content delivery.


Here are our insights on what jobs will be changed by gen AI and how media & entertainment companies should handle the change.

Evolution, not elimination
While gen AI will replace specific routine tasks, the technology will more often complement human capabilities. That’s especially important for the media & entertainment industry, in which creativity, storytelling, and the magic of human imagination are at the heart of a brand.

In animation departments, for example, gen AI could automate repetitive tasks like background rendering or character movement. However, skilled animators would still be essential for creating unique characters, infusing emotion into scenes, and maintaining the overall creative vision of the animation.

And in the field of application development, gen AI can automate such tasks as generating boilerplate code and identifying patterns. However, developers' expertise will remain crucial for designing complex algorithms, optimizing performance, and ensuring user-friendly interfaces.

Skillsets and roles
While some roles will evolve in the generative AI era, other new ones will arise. We envision new jobs that require expertise in managing gen AI systems, interpreting gen AI-generated content, and ensuring ethical and responsible use of the technology.

For example, as the industry explores AI-generated storytelling, there could emerge a need for AI story analysts. These professionals would review and refine AI-generated storylines, ensuring they align with a company’s brand and narrative standards—while adding a human touch.

And in the legal department, generative AI can assist in contract review and legal research, which will lead to the emergence of the gen AI legal analyst, responsible for overseeing AI-generated legal documents, ensuring compliance, and addressing ethical concerns.

A collaborative effort
One fascinating aspect of gen AI will be an increasingly symbiotic relationship between humans and the technology to enhance productivity and innovation.


In quality assurance testing, for example, gen AI-powered tools can perform routine testing procedures, detecting basic bugs. QA testers can then focus on intricate exploratory testing, user experience assessment, and edge cases that require human intuition.

Meanwhile, in theme park management, gen AI could be employed to optimize ride wait times based on real-time data. Staff members would collaborate with the systems to interpret the data, make strategic adjustments, and create personalized experiences for visitors.

Navigating the change: best practices
Media & entertainment enterprises are looking at a tumultuous period as they fold gen AI into their operations. Here are some best practices to minimize disruption and build value:

1.    Help the workforce learn and adapt
Leaders should emphasize the importance of lifelong learning and adaptation. Individuals should be empowered to upskill and reskill, enabling them to remain valuable contributors in a rapidly evolving work environment. For media & entertainment companies, this might mean encouraging IT professionals to stay up to date with evolving generative AI technologies. They could upskill and specialize, for example, by learning to implement gen AI-based cybersecurity measures.

Businesses should also offer workshops in which creators learn to use gen AI-powered tools for concept art, allowing them to experiment while maintaining their unique artistic styles.

In general, training programs should be tailored to address specific skill gaps within departments, aligning with each department's objectives. Leaders should encourage collaboration between departments to foster knowledge sharing and interdisciplinary skill development.

Media & entertainment companies need to establish reskilling and upskilling initiatives that help employees transition into new roles or acquire skills relevant to the evolving job landscape. This could involve online learning platforms; companies could partner with such platforms to provide courses on gen AI ethics, storytelling, and more. This would empower employees, such as scriptwriters, to understand the nuances of AI-generated content and adapt their creative processes accordingly.

Job redesign, too, will be important. Companies should focus on redesigning roles to capitalize on human strengths that gen AI cannot replicate, such as empathy, creativity, complex decision-making, and ethical judgment. In the marketing department, while gen AI might handle data analysis to identify target audiences, human marketers would apply their creativity to craft emotionally resonant campaigns that resonate with their audience.

2.    Transparency and communication
Media & entertainment firms should foster transparent communication regarding the integration of gen AI into the organization. That means addressing stakeholders’ concerns and sharing the rationale behind gen AI adoption.

For example, when gen AI-generated legal documents are employed, the legal team should transparently communicate how the tech contributes to drafting contracts more efficiently, ensuring clarity, while emphasizing that legal experts still provide the critical analysis and decision-making.

And for any in-person event, it’s vital to highlight how generative AI is enhancing the guest experience. Businesses must explain how algorithms assist in predicting visitor preferences, leading to more personalized recommendations for attractions and merchandise.

3.    Get employees involved
It’s crucial to involve employees in the gen AI integration process. They should be encouraged to contribute ideas on how the technology can be leveraged to streamline tasks and create new opportunities, fostering a sense of ownership and collaboration. Application developers could hold brainstorming sessions, for example, in which developers collaborate with generative AI systems to ideate and prototype new features, enhancing creativity and innovation. 

Companies should also establish cross-functional teams comprising animators, data analysts, and generative AI specialists to collaboratively develop new interactive experiences that seamlessly blend AI-generated content with traditional storytelling.

Opportunities ahead
Generative AI offers opportunities for increased efficiency, optimization of processes, and the allocation of human resources to more strategic tasks.

But the technology must be approached in a discerning fashion—especially by media & entertainment companies, for which creativity is the keystone. While efficiency gains are possible, there are considerations that demand thoughtful management. The potential for job displacements in certain areas necessitates a strategic approach to workforce planning and the need for reskilling initiatives to ensure a smooth transition for affected employees.



'''





def content_generation(r1,r2,r3,Topic, finalized_keyword, content_type):
    results = []

    if "Title" in content_type:
        system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        -----------------------------------------------
        Instruction : You have to strictly generate only one title.
        '''
        user_prompt_title = f'Write one descriptive title for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 50-60 characters.'
        response_title = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_title}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        results.append("Title:\n" + response_title.choices[0].message['content'])

    if "Meta Description" in content_type:
        system = '''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        
        ---------------------------------------
        Instructions: You have to strictly generate only one meta description.
        '''
        user_prompt_meta = f'Write one descriptive Meta Description for the topic {Topic} and optimize it for keywords {finalized_keyword} with character limit of 150 -160 characters.'
        response_meta = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt_meta}
            ],
            temperature=0.8,
            max_tokens=5000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        results.append("Meta Description:\n" + response_meta.choices[0].message['content'])
    
    
    
    if "Alt Text" in content_type:
        system = '''You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        '''
        user_prompt = f'''Generate 5 ideas for images with ALT text that can be added on blog post for the topic : {Topic} And optimize it for the keyword : {finalized_keyword} for SEO.
            Give me a table with column names as Idea, Idea Description and ALT text.
            '''
              
            
        response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        results.append("Alt Text:\n" + response.choices[0].message['content'])
    
    
    
    return "\n\n".join(results)

def style_generation(ref1,ref2,ref3,Topic,Title, finalized_keyword,style):
    results=[]
    
    if "Style1- Weekly Tech Blog" in style:
        system12=f'''
        You have expertise in linguistics, natural language processing, and prompt engineering.
        Your task is to convert the provided text into an elaborate style guide. 
        This guide will serve as a blueprint for creating fresh content on a distinct topic while maintaining the original style demonstrated in the text.
        Pay special attention to aspects like:

        1. The voice and tone: How formal or casual is the language? Is it authoritative, friendly, neutral, or something else?
        2. Mood: What emotional atmosphere is created? Does the text seem cheerful, melancholic, mysterious, etc.?
        3. Sentence structure: Are the sentences simple, compound, complex, or a mixture? How long are they typically?
        4. Transition style: How does the writer navigate from one idea to another? What types of transition words or phrases are used?
        5. Rhythm and pacing: Is the writing fast-paced with lots of short sentences, or is it slow and deliberate with longer sentences?
        6. Signature styles: Are there any recurring phrases or unique punctuation usage that stands out? Any patterns or repetitions?
        I am particularly interested in the stylistic nuances that set this authors writing apart. 

        Identify those elements that could serve as indicators of this authors distinctive writing style.
        
        '''

        def content__style_guide_extraction1(ref_s1):
            user_prompt= f"This is the text : {ref_s1} you have to analyze and provide detailed style guide based on the outlined features."
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result

    
        def content__style_guide_extraction2(ref_s2):
            user_prompt = f'''
            This is the text : {ref_s2} you have to analyze and provide detailed style guide based on the outlined features.
            ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result
    
        def content__style_guide_extraction3(ref_s3):
            user_prompt = f'''
            This is the text : {ref_s3} you have to analyze and provide detailed style guide based on the outlined features.
            ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  
    
            return result
    

        def final_output(prev1,prev2,prev3):
            system1='''
    
    You have an expertise in linguistics, natural language processing, technical writing, and prompt engineering.
    Your task is to convert the following analyses of an authors writing into an elaborate, detailed style guide. 
    This guide will serve as a blueprint for creating fresh content on a distinct topic while maintaining the original style demonstrated in the analyzed texts.
    In final response you will give the single style guide which will come after evaluating all the analysis.
    '''
            user_prompt = f'''
     Combine all three analyses : {prev1},{prev2},{prev3} , and synthesize them into a single, unified style guide.
    ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system1},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result
    
        def article_style_guide(style_guide,Topic,finalized_keyword):
            system=f'''
        You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
        and catered to clients across all sectors.
        
        Your task is to first write a blog post using this style guide only : {style_guide} then you will criticize your blog post and finally give correct blog post. 
        Instructions:
        - You have to strictly extract the format of blog post by reading line by line these blog post: {t_blog1},{t_blog2},{t_blog3} and use this format while writting new blog post.
        - You have to strictly give the correct blog post only in output.  
            
        
        '''
#-------------------------Instructions:- Your task is to write a article using this style guide only {style_guide}.
        
            user_prompt = f'Write a blog post by considering these blog post {ref1},{ref2},{ref3} using this style guide {style_guide} on this topic : {Topic}, Title: {Title} and optimize it for keywords {finalized_keyword} for SEO.'
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result

    
        def result(t_blog1,t_blog2,t_blog3,t,k):
            prev1=content__style_guide_extraction1(t_blog1) # content1
            prev2=content__style_guide_extraction2(t_blog2) # 
            prev3=content__style_guide_extraction3(t_blog3) # 
            final_response=final_output(prev1,prev2,prev3)  # single style guide after analyzing all the three above
            article=article_style_guide(final_response,t,k) # article generation using above final style guide
            return article
        
        results.append("Weekly Tech Blog:\n" + result(t_blog1,t_blog2,t_blog3,Topic,finalized_keyword))
    
    
    if "Style2- Descriptive Blog" in style:
        system12=f'''
        You have expertise in linguistics, natural language processing, and prompt engineering.
        Your task is to convert the provided text into an elaborate style guide. 
        This guide will serve as a blueprint for creating fresh content on a distinct topic while maintaining the original style demonstrated in the text.
        Pay special attention to aspects like:

        1. The voice and tone: How formal or casual is the language? Is it authoritative, friendly, neutral, or something else?
        2. Mood: What emotional atmosphere is created? Does the text seem cheerful, melancholic, mysterious, etc.?
        3. Sentence structure: Are the sentences simple, compound, complex, or a mixture? How long are they typically?
        4. Transition style: How does the writer navigate from one idea to another? What types of transition words or phrases are used?
        5. Rhythm and pacing: Is the writing fast-paced with lots of short sentences, or is it slow and deliberate with longer sentences?
        6. Signature styles: Are there any recurring phrases or unique punctuation usage that stands out? Any patterns or repetitions?
        I am particularly interested in the stylistic nuances that set this authors writing apart. 

        Identify those elements that could serve as indicators of this authors distinctive writing style.
        
        '''
    
        def content__style_guide_extraction1(ref_s1):
    
            user_prompt= f"This is the text : {ref_s1} you have to analyze and provide detailed style guide based on the outlined features."
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result

    
        def content__style_guide_extraction2(ref_s2):
            user_prompt = f'''
                This is the text : {ref_s2} you have to analyze and provide detailed style guide based on the outlined features.
                    ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
            )
            result=response.choices[0].message['content']  

            return result
        
    
    
        def content__style_guide_extraction3(ref_s3):
            user_prompt = f'''
            This is the text : {ref_s3} you have to analyze and provide detailed style guide based on the outlined features.
            ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system12},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
            )
            result=response.choices[0].message['content']  
    
            return result
    

        def final_output(prev1,prev2,prev3):
            system1='''

            You have an expertise in linguistics, natural language processing, technical writing, and prompt engineering.
            Your task is to convert the following analyses of an authors writing into an elaborate, detailed style guide. 
            This guide will serve as a blueprint for creating fresh content on a distinct topic while maintaining the original style demonstrated in the analyzed texts.
            In final response you will give the single style guide which will come after evaluating all the analysis.
    '''
            user_prompt = f'''
        Combine all three analyses : {prev1},{prev2},{prev3} , and synthesize them into a single, unified style guide.
        ''' 
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system1},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result
    
        def article_style_guide(style_guide,Topic,finalized_keyword):
            system=f'''
                You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
                and catered to clients across all sectors.
                
                Your task is to first write a blog post using this style guide only : {style_guide} then you will criticize your blog and and finally give correct blog post.
                Instructions:
                - You have to strictly extract the format of blog post by reading line by line these blog post: {d_blog1},{d_blog2},{d_blog3} and use this format while writting new blog post.
                - You have to strictly give the correct blog post in output only.
                '''

        
            user_prompt = f'Write a blog post by considering these blog post {ref1},{ref2},{ref3} using this style guide {style_guide} on this topic {Topic} , Title : {Title} and optimize it for keywords {finalized_keyword} for SEO.'
            response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=4000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
            result=response.choices[0].message['content']  

            return result

    
        def result(a,b,c,t,k):
            prev1=content__style_guide_extraction1(d_blog1) # content1
            prev2=content__style_guide_extraction2(d_blog2) # 
            prev3=content__style_guide_extraction3(d_blog3) # 
            final_response=final_output(prev1,prev2,prev3)  # single style guide after analyzing all the three above
            article=article_style_guide(final_response,t,k) # article generation using above final style guide
            return article
            
        results.append("Descriptive Blog:\n" + result(d_blog1,d_blog2,d_blog3,Topic,finalized_keyword))
    
    if "Style3- Glossary" in style:
        system = '''

            You are a SEO Expert and your client is  an IT organisation which deals in these core services : IT consulting, business process outsourcing, digital transformation, application development, artificial intelligence, cloud services, data analytics, quality assurance, and IT infrastructure services.
            and catered to clients across all sectors.
            
        '''
        user_prompt = f'Generate 5 FAQs on {Topic} and optimize it for {finalized_keyword} for SEO. Explain FAQs in 100-150 words.'
        response = openai.ChatCompletion.create(
            engine="AIKillsSEO",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.8,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        results.append("Glossary :\n" + response.choices[0].message['content'])
    
    return "\n\n".join(results)




css = """
.tabs {
  border-radius: 0.5rem 0.5rem 0 0;
  padding-left: 0;
  margin-bottom: 0;
}
.tab-nav {
  display: flex;
  -webkit-box-flex: 1;
  -ms-flex-positive: 1;
  flex-grow: 1;
  background-color: #e5eff9;
  border-top: 1px solid #d0d0ce;
  border-right: 1px solid #d0d0ce;
  border-top-right-radius: 0.5rem;
  border-top-left-radius: 0.5rem;
}
.tabs .tab-nav button:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 10px;
}
.tabs .tab-nav button {
  padding: 0.75rem 1.25rem;
  border-radius: inherit;
  color: #2f78c4;
  cursor: pointer;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out;
  background: none;
  border: none;
  cursor: pointer;
}

.tabs .tab-nav button.selected:first-child {
  border-top-left-radius: 0.5rem;
  border-left: 1px solid #d0d0ce;
}

.tabs .tab-nav button:hover:not(.selected) {
  background: #fff;
  border-radius: 0;
}

.tabs .tab-nav button.selected {
  color: #000048;
  font-size: 20px;
  font-weight: 700;
  padding: 15px 25px;
  margin-bottom: -1px;
  box-shadow: inset 0 4px 0 0 #2f78c4, 0 0px 0 0 #ffffff;
  padding: 0.75rem 1.25rem;
  background: #fff;
  border-bottom: none;
}
.tabs .tab-nav button.selected:not(:first-child) {
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.tabs .tab-item {
  background: #fff;
  border-radius: 0 0 0.5rem 0.5rem;
  border: 1px solid #d0d0ce;
  border-width: 1px;
  padding: 1.25rem;
}

button.lg {
  width: 100%;
  text-align: center;
  margin: 0 0.5rem 1rem 0rem !important;
  padding: 0.75em 1.25em !important;
  border: none !important;
  border-radius: 500em !important;
  -webkit-transition: background 0.25s ease-out, color 0.25s ease-out,
    border-color 0.25s ease-out;
  transition: background 0.25s ease-out, color 0.25s ease-out,
    border-color 0.25s ease-out;
  -webkit-appearance: none;
  line-height: 1;
  font-weight: bold;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: reverse;
  -ms-flex-direction: row-reverse;
  flex-direction: row-reverse;
  background: #26efe9 !important;
  color: #000048 !important;
}
button.lg {
  font-size: 1.25rem !important;
}
button.lg:hover {
  background: #a8f9f6 !important;
}

label {
  display: block;
  margin: 0;
  font-size: 1rem;
  font-weight: normal;
  line-height: 1.8;
  color: #000048;
}

textarea {
  width: 100% !important;
  padding: 0.85rem 0.5rem 0.85rem 1rem !important;
  color: #000048 !important;
  border: 0.05rem solid #97999b !important;
  border-radius: 0.5rem !important;
  background: #f5f5f2 !important;
}
input[type="checkbox"] {
  margin-right: 0.5rem;
  margin-bottom: 0;
  box-sizing: border-box;
  padding: 0;
  position: relative;
  margin: 0 0.5rem 0 0;
  cursor: pointer;
}
input[type="checkbox"]:checked::before {
  transform: rotate(-45deg) scale(1, 1);
}
input[type="checkbox"]:checked::after {
  border-color: #2f78c4;
  background: #2f78c4;
}
input[type="checkbox"]::after {
  border-radius: 0.2em;
  position: absolute;
  top: -4px;
  left: -2px;
  width: 20px;
  height: 20px;
  content: "";
  cursor: pointer;
  border: 0.12rem solid #6aa2dc;
  background: #ffffff;
  box-shadow: inset 0 1px 2px rgba(0, 0, 72, 0.2);
}
input[type="checkbox"]::before {
  position: absolute;
  z-index: 1;
  top: 2px;
  left: 2px;
  width: 12px;
  height: 6px;
  content: "";
  transition: transform 0.4s cubic-bezier(0.45, 1.8, 0.5, 0.75);
  transform: rotate(-45deg) scale(0, 0);
  border: 2px solid #ffffff;
  border-top-style: none;
  border-right-style: none;
}

.form fieldset label {
  display: inline;
}
fieldset label span ,label span,fieldset span {
  margin-right: 0.25rem;
  color: #000048 !important;
  
}
h1 {
  font-weight: 600;
  line-height: 1.25;
  color: #000048;
  margin: 1rem 0 !important;
  font-size: 47px !important;
}
footer .svelte-1ax1toq{
  display: none !important
}

""" 
with gr.Blocks(css=css) as demo:
    #gr.Markdown("Automate the whole SEO process using GPT4")
    gr.HTML('<a href="https://www.cognizant.com/in/en" aria-label="Cognizant-logo"><img aria-label="Cognizant Logo" alt="Cognizant Logo" width="250" height="45" src="https://cognizant.scene7.com/is/content/cognizant/COG-Logo-2022-8?fmt=png-alpha" /></a>')
    gr.HTML("<h1>Automate the whole SEO process using GPT4</h1>")
    #gr.Image("https://placehold.co/600x400")
    

    with gr.Tab("Topic Generation Using Reference Content"):
        content_input1=gr.TextArea(label="Reference Content1")
        content_input2=gr.TextArea(label="Reference Content2")
        content_input3=gr.TextArea(label="Reference Content3")
        Selection=gr.CheckboxGroup(["Topic"])
        content_output1=gr.TextArea(label="Generated Text")
        content_button=gr.Button("Submit")
    with gr.Tab("Keyword generation"):
        text_input1=gr.TextArea(label=" Enter the topic you want to write for")
        keyword_selection1=gr.CheckboxGroup(["Similar Keyword","Long Tail Keyword","Short tail Keyword","Semantically Related"])
        text_output1=gr.TextArea(label="Generated keyword")
        submit_button1=gr.Button("Submit")
    #with gr.Tab("Keyword Analysis"):
        #text_input2=gr.Textbox(label="Enter the Keyword.")
        #text_output2=gr.Textbox(label="Report")
        #submit_button2=gr.Button("Submit")
    with gr.Tab("Generating Content for finalized Keyword"):
        #topic_input3=gr.Textbox(label="Enter the topic")
        text_input3=gr.TextArea(label="Enter the finalized Keyword")
        select_option3=gr.CheckboxGroup(["Title","Meta Description","Alt Text"])
        text_output3=gr.TextArea(label="Generated Content")
        submit_button3=gr.Button("Submit")
    
   # with gr.Tab("Gnerating outlines based on type of content"):
    #    type_of_content=gr.CheckboxGroup(["Blog post"])
     #   content_output=gr.Textbox(label="Generated Outlines")
      #  content__guide_button=gr.Button("Submit")
    with gr.Tab("Blog Post Generation"):
        #text_input4=gr.Textbox(label="Enter Topic")
        key_input4=gr.TextArea(label="Enter Title")
        select_option4=gr.CheckboxGroup(["Style1- Weekly Tech Blog","Style2- Descriptive Blog","Style3- Glossary"])
        text_output4=gr.TextArea(label="Generated Content")
        submit_button4=gr.Button("Submit")
    
    #with gr.Tab("FAQ/Alt Text  Idea Generation"):
        #text_input8=gr.Textbox(label="Enter the topic")
        #key_gen8=gr.Textbox(label="Enter the finalized Keyword")
        #select_option=gr.CheckboxGroup(["FAQ","Alt Text"])
        #out8=gr.Textbox(label="Generated Content")
        #submit_button8=gr.Button("Submit")
    #with gr.Tab("Palgarism Check"):
        #text_input5=gr.Textbox(label="give the content you want to check")
        #text_output5=gr.Textbox(label="Report")
        #submit_button5=gr.Button("Submit")
    #with gr.Tab("Post Publishing Analysis"):
        #text_input6=gr.Textbox(label="give the URL")
        #text_output6=gr.Textbox(label="Report")
        #submit_button6=gr.Button("Submit")
    

    
    submit_button1.click(generate_keywords,inputs=[content_input1,content_input2,content_input3,text_input1,keyword_selection1],outputs=text_output1)
    submit_button3.click(content_generation,inputs=[content_input1,content_input2,content_input3,text_input1,text_input3,select_option3],outputs=text_output3)
    submit_button4.click(style_generation,inputs=[content_input1,content_input2,content_input3,text_input1,key_input4,text_input3,select_option4],outputs=text_output4)
    #submit_button8.click(idea_generator,inputs=[text_input1,text_input3,select_option],outputs=out8)
    content_button.click(content_extraction,inputs=[content_input1,content_input2,content_input3,Selection],outputs=content_output1)
    #content__guide_button.click(content__style_guide_extraction,inputs=[content_input1,content_input2,content_input3,type_of_content,text_input1,text_input3],outputs=content_output)


demo.queue().launch(server_name="0.0.0.0", server_port=8080)
