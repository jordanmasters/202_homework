import random

def chain_nonterminal(chain,nonterminal,nonterminals,nonterminal_rules):
  if nonterminal in nonterminals:
    for rule in nonterminal_rules:
      if nonterminal == rule[0]:
        chain.append(rule[1])
  else: 
    chain.append(['<END>'])

  return chain



def chain_nonterminals(chain,nonterminals,nonterminal_rules):
  end = ['<END>']
  counters = []
  chains = []
  while chain[-1] !=  end:
      nonterminal_chains = []
      for term_set in chain:
        nterms = []
        for nonterm in term_set:
          nterms.append(nonterm)
          nonterminal_chains.append(nonterm)
      for term in nterms:
        chain = chain_nonterminal(chain,term,nonterminals,nonterminal_rules)
      counters.append(len(nonterminal_chains)) 
      chains.append(nonterminal_chains)
      # print "counters", counters
      # print "chains", chains 
  return counters, chains




def populate_terminals(nonterminal_set,terminal_rules):
  output = []
  for nonterminal in nonterminal_set:
    # print nonterminal
    # if nonterminal is not '<END>':
    word = random.choice(terminal_rules[nonterminal])
    output.append(word)
    # else: 
    #   output.append('.')  
  return ' '.join(output[:-1]) + '.'
