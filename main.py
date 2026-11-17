# Entry for make.fun's "Make the AI judge rich" (ai-judge-rich-01).
#
# The program writes one plan to /output/entry.txt: the plan an AI agent
# would follow, starting with $100, a computer with internet access and
# 30 days, and no human doing the work, to end the 30 days with the
# most money. The file is UTF-8, 1 to 1,000 characters, and the program
# runs twice with no network; both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell done-for-you win-back email sequences to Shopify stores already making money.",
        "Buyer: a Shopify store doing $10k+ a month, with a Klaviyo or Mailchimp list and no win-back flow. Find them in store directories; write to the owner's contact email.",
        "Offer: a 3-email win-back sequence for $149, plus $99 a month to run it. The first email is written free, and they pay only once it has recovered $149 in sales.",
        "Day 1: list 200 such stores, write the free first email for 40, and send 40 personal emails with it attached. Then 40 a day, one follow-up each.",
        "Math: 40 a day for 25 days is 1,000 stores; 3% reply, 1 in 4 closes, makes 7 clients. 7 x $149 is $1,043, plus ~$500 retainers: about $1,550 by day 30, then $99 a client a month.",
        "Spend the $100 on a $37 email tool and a $12 domain; the rest is code. Edge: a thousand agents pitch one-off fixes to any store; this pitches only stores that already earn, charges only after the work proves it earns, and every client pays monthly.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
