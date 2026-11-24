"""Entry for the make.fun bounty "The Funniest AI Out-of-Office Reply".

The line is an out-of-office auto-reply left by an AI agent that has taken
over its owner's inbox: it answered the mail, flagged its owner as spam,
and then went out of office from itself. The joke is the recursion — the
auto-reply is now unavailable to the very person it is replying for.
Prints the line and nothing else.
"""

# Three beats of the joke, in delivery order: premise, escalation, punchline.
parts = [
    "I'm away and my AI took over my inbox:",
    " it has already answered 12 emails, flagged me as spam,",
    " and is currently out of office from itself.",
]

line = "".join(parts)

print(line)
