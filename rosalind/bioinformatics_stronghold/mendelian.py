import pdb
def probability_dominent(homo_dom=0, hetero=0, homo_rec=0):
  '''returns the probability of random mating producing a dominent individual'''
  total_in_population = float(homo_dom + hetero + homo_rec)
  if total_in_population < 2:
    return 0

  # homo_dom_dom_alleles = 2*homo_dom
  # homo_rec_dom_alleles = 0
  # hetero_dom_alles = hetero

  # total_dom_alles_in_population = homo_dom_dom_alleles + homo_rec_dom_alleles + hetero_dom_alles
  # if homo_dom==1 and homo_rec==1:
  #   pdb.set_trace()

  prob_homo_dom_x_homo_dom = homo_dom/total_in_population * (max(0,homo_dom-1))/(total_in_population-1)
  prob_homo_dom_x_homo_rec = homo_dom/total_in_population * homo_rec/(total_in_population-1)
  prob_homo_dom_x_hetero   = homo_dom/total_in_population * hetero/(total_in_population-1)
  prob_homo_rec_x_homo_rec = homo_rec/total_in_population * (max(0,homo_rec-1))/(total_in_population-1)
  prob_homo_rec_x_hetero = homo_rec/total_in_population * hetero/(total_in_population-1)
  prob_homo_rec_x_homo_dom = homo_rec/total_in_population * homo_dom/(total_in_population-1)
  prob_hetero_x_hetero = hetero/total_in_population * (max(0,hetero-1))/(total_in_population-1)
  prob_hetero_x_homo_dom = hetero/total_in_population * homo_dom/(total_in_population-1)
  prob_hetero_x_homo_rec = hetero/total_in_population * homo_rec/(total_in_population-1)

  return prob_homo_dom_x_homo_dom*1 + \
  prob_homo_dom_x_homo_rec*1 +        \
  prob_homo_dom_x_hetero*1 +          \
  prob_homo_rec_x_homo_rec*0 +        \
  prob_homo_rec_x_hetero*0.5 +        \
  prob_homo_rec_x_homo_dom*1 +        \
  prob_hetero_x_hetero*0.75  +        \
  prob_hetero_x_homo_dom*1   +        \
  prob_hetero_x_homo_rec*0.5
  
