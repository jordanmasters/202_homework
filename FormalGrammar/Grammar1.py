import random
import Grammar1_tools
# the non terminals
nonterminals = ['paragraph','<sentence>', '<noun phrase>', '<noun>', '<det>', '<verb>']

# the teminals
terminals = ['the', 'frog', 'dog','ran','log','man','hog','can','plan']

# the starting points
seed = '<sentence>'



# the rules
nonterminal_rules = [ 
['<sentence>',              ['<noun phrase>', '<verb phrase>']],
['<noun phrase>',           ['<det>','<noun>']],            
['<verb phrase>',           ['<verb>','<det>','<noun>','<END>']],            
]
nonterminals = [x[0] for x in nonterminal_rules]

terminal_rules = { 
  '<det>': ['the'],
  '<noun>': ['frog','dogs','log','hogs','man','can','plan'],
  '<verb>': ['ran','dogs','logs','hogs','man','plan'],
  '<END>': ['.'],
}

# the primary building chain data
chain = []

# chain seed to second layer of non-terminals
chain = Grammar1_tools.chain_nonterminal(chain,seed,nonterminals,nonterminal_rules)

# Now that chain has been seeded, run through the dependency tree and until we hit the end
# output a counter and chain for each level of the tree
counters,chains = Grammar1_tools.chain_nonterminals(chain,nonterminals,nonterminal_rules)

# take the terminal chain from chains and remove generational build-up
nonterminal_set = chains[-1][counters[-2]:]

# print example sentences
for i in range(10):
    print Grammar1_tools.populate_terminals(nonterminal_set,terminal_rules)

