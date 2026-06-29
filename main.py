from src.extractive_summarizer import extractive_summary
from src.abstractive_summarizer import abstractive_summary

text = """The Revolt of 1857, also known as the Indian
Mutiny or the First War of Independence, has been
a subject of historical analysis from various
scholarly perspectives.
• Nationalist Perspective: Many Indian
nationalist scholars view the Revolt of 1857 as
a significant precursor to the broader struggle
for independence. They argue that it was a
collective uprising against British colonial rule
and symbolizes the early aspirations for selfrule. Historians like Bipan Chandra and R.C.
Majumdar have highlighted the nationalistic
character of the revolt.
• Marxist Perspective: Marxist historians,
including Irfan Habib, interpret the Revolt of
1857 as a manifestation of class struggle. They
argue that it was driven by socio-economic
factors, with the Indian peasantry and soldiers
revolting against the oppressive colonial
policies and economic exploitation. According
to this perspective, the revolt represented the
awakening of the rural masses against British
imperialism.
• Colonial Perspective: From a colonial
perspective, British historians traditionally
portrayed the events of 1857 as a "mutiny"
rather than a war of independence. They often
emphasized the role of mutinous sepoys
(Indian soldiers) and saw it as a challenge to
British authority that was effectively
suppressed.
• Revisionist Perspective: Revisionist historians
have challenged some of the conventional
narratives surrounding the Revolt of 1857.
They argue that the revolt was not necessarily
a unified, coordinated struggle for
independence but rather a series of localized
and diverse uprisings with varying motivations.
Scholars like Christopher Bayly have explored
the complexities of the revolt.
Savarkar's Perspective (War of Independence):
Vinayak Damodar Savarkar, in his book "First War
of Indian Independence," argued that the Revolt of
1857 should be recognized as the "First War of
Independence." He emphasized the coordinated
efforts of various Indian communities, including
sepoys, peasants, and intellectuals, against British
rule. Savarkar believed that the revolt had a
nationalistic character and laid the foundation for
subsequent freedom struggles. His perspective
aligns with the nationalist interpretation of the
event.
It's important to note that the interpretation of the
Revolt of 1857 continues to be a subject of debate
and discussion among historians, with various
perspectives offering nuanced insights into this
pivotal moment in India's history"""

print("Extractive Summary:\n", extractive_summary(text))
print("\nAbstractive Summary:\n", abstractive_summary(text))