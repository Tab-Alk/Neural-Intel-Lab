
PERSPECTIVE

# A critique of pure learning and what artificial neural networks can learn from animal brains

Anthony M. Zador1

Artificial neural networks (ANNs) have undergone a revolution, catalyzed by better supervised learning algorithms. However, in stark contrast to young animals (including humans), training such networks requires enormous numbers of labeled examples, leading to the belief that animals must rely instead mainly on unsupervised learning. Here we argue that most animal behavior is not the result of clever learning algorithms—supervised or unsupervised—but is encoded in the genome. Specifically, animals are born with highly structured brain connectivity, which enables them to learn very rapidly. Because the wiring diagram is far too complex to be specified explicitly in the genome, it must be compressed through a “genomic bottleneck.” The genomic bottleneck suggests a path toward ANNs capable of rapid learning.

Not long after the invention of computers in the 1940s, expectations were high. Many believed that computers would soon achieve or surpass human-level intelligence. Herbert Simon, a pioneer of artificial intelligence (AI), famously predicted in 1965 that “machines will be capable, within twenty years, of doing any work a man can do”—to achieve general AI. Of course, these predictions turned out to be wildly off the mark.

In the tech world today, optimism is high again. Much of this renewed optimism stems from the impressive recent advances in artificial neural networks (ANNs) and machine learning, particularly “deep learning”1. Applications of these techniques—to machine vision, speech recognition, autonomous vehicles, machine translation and many other domains—are coming so quickly that many predict we are nearing the “technological singularity,” the moment at which artificial superintelligence triggers runaway growth and transforms human civilization2. In this scenario, as computers increase in power, it will become possible to build a machine that is more intelligent than the builders. This superintelligent machine will build an even more intelligent machine, and eventually this recursive process will accelerate until intelligence hits the limits imposed by physics or computer science.

But in spite of this progress, ANNs remain far from approaching human intelligence. ANNs can crush human opponents in games such as chess and Go, but along most dimensions—language, reasoning, common sense—they cannot approach the cognitive capabilities of a four-year-old. Perhaps more striking is that ANNs remain even further from approaching the abilities of simple animals. Many of the most basic behaviors—behaviors that seem effortless to even simple animals—turn out to be deceptively challenging and out of reach for AI. In the words of one of the pioneers of AI, Hans Moravec3:

“Encoded in the large, highly evolved sensory and motor portions of the human brain is a billion years of experience about the nature of the world and how to survive in it. The deliberate process we call reasoning is, I believe, the thinnest veneer of human thought.”

1Cold Spring Harbor Laboratory, Cold Spring Harbor, NY 11724, USA. Correspondence and requests for materials should be addressed to A.M.Z. (email: zador@cshl.edu)


NATURE COMMUNICATIONS | (2019) 10:3770  | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications

---

PERSPECTIVE

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6

effective only because it is supported by this much older and much more powerful, though usually unconscious, sensorimotor knowledge. We are all prodigious Olympians in perceptual and motor areas, so good that we make the difficult look easy. Abstract thought, though, is a new trick, perhaps less than 100 thousand years old. We have not yet mastered it. It is not all that intrinsically difficult; it just seems so when we do it.

# Learning by ANNs

In the earliest days of AI, there was a competition between two approaches: symbolic AI and ANNs. In the symbolic “good old fashion AI” approach championed by Marvin Minsky and others, it is the responsibility of the programmer to explicitly program the algorithm by which the system operates. In the ANN approach, by contrast, the system “learns” from data. Symbolic AI can be seen as the psychologist’s approach—it draws inspiration from the human cognitive processing, without attempting to crack open the black box—whereas ANNs, which use neuron-like elements, take their inspiration from neuroscience. Symbolic AI was the dominant approach from the 1960s to 1980s, but since then it has been eclipsed by ANN approaches inspired by neuroscience.

Modern ANNs are very similar to their ancestors three decades ago. Much of the progress can be attributed to increases in raw computer power: Simply because of Moore’s law, computers today are several orders of magnitude faster than they were a generation ago, and the application of graphics processors (GPUs) to ANNs has sped them up even more. The availability of large data sets is a second factor: Collecting the massive labeled image sets used for training would have been very challenging before the era of Google. Finally, a third reason that modern ANNs are more useful than their predecessors is that they require even less human intervention. Modern ANNs—specifically “deep networks”—learn the appropriate low-level representations (such as visual features) from data, rather than relying on hand-wiring to explicitly program them in.

In ANN research, the term “learning” has a technical usage that is different from its usage in neuroscience and psychology. In ANNs, learning refers to the process of extracting structure—statistical regularities—from input data, and encoding that structure into the parameters of the network. These network parameters contain all the information needed to specify the network. For example, a fully connected network with N neurons might have one parameter (e.g., a threshold) associated with each neuron, and an additional N2 parameters specifying the strengths of synaptic connections, for a total of N + N2 free parameters. Of course, as the number of neurons N becomes large, the total parameter count in a fully connected ANN is dominated by the N2 synaptic parameters.

There are three classic paradigms for extracting structure from data, and encoding that structure into network parameters (i.e., weights and thresholds). In supervised learning, the data consist of pairs—an input item (e.g., an image) and its label (e.g., the word “giraffe”)—and the goal is to find network parameters that generate the correct label for novel pairs. In unsupervised learning, the data have no labels; the goal is to discover statistical regularities in the data without explicit guidance about what kind of regularities to look for. For example, one could imagine that with enough examples of giraffes and elephants, one might eventually infer the existence of two classes of animals, without the need to have them explicitly labeled. Finally, in reinforcement learning, data are used to drive actions, and the success of those actions is evaluated based on a “reward” signal.

Much of the progress in ANNs has been in developing better tools for supervised learning. A central consideration in supervised learning is “generalization.” As the number of parameters increases, so too does that “expressive power” of the network.


NATURE COMMUNICATIONS | (2019) 10:3770 | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications

---
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6
# PERSPECTIVE

What is the next number 2, 4, 6, 8, ? There are only 107 s in a year, so a child would need to ask one question every second of her life to receive a comparable volume of labeled data; and of course, most images encountered by a child are not labeled. There is, thus, a mismatch between the available pool of labeled data and how quickly children learn. Clearly, children do not rely mainly on supervised algorithms to learn to categorize objects.

Considerations such as these have motivated the search in the machine learning community for more powerful learning algorithms, for the “secret sauce” posited to enable children to learn how to navigate the world within a few years. Many in the ANN community, including pioneers such as Yann Lecun and Geoff Hinton, posit that instead of supervised paradigms, we rely instead primarily on unsupervised paradigms to construct representations of the world. In the words of Yann Lecun:

“If intelligence is a cake, the bulk of the cake is unsupervised learning, the icing on the cake is supervised learning, and the cherry on the cake is reinforcement learning.”

Because unsupervised algorithms do not require labeled data, they could potentially exploit the tremendous amount of raw (unlabeled) sensory data we receive. Indeed, there are several unsupervised algorithms which generate representations reminiscent of those found in the visual system. Although at present these unsupervised algorithms are not able to generate visual representations as efficiently as supervised algorithms, there is no known theoretical principle or bound that precludes the existence of such an algorithm (although the No-Free-Lunch theorem for learning algorithms states that no completely general-purpose learning algorithm can exist, in the sense that for every learning model there is a data distribution on which it will fare poorly). Every learning model must contain implicit or explicit restrictions on the class of functions that it can learn.

Thus, while the number of labeled images a child encounters during her first 107 s of life might be small, the total sensory input received during that time is quite large; perhaps Nature has evolved a powerful unsupervised algorithm to exploit this large pool of data. Discovering such an unsupervised algorithm—if it exists—would lay the foundation for a next generation of ANNs.

# Learning by animals

# Learned and innate behavior in animals

The term “learning” in neuroscience (and in psychology) refers to a long-lasting change in behavior that is the result of experience. Learning in this context encompasses animal paradigms such as classical and operant conditioning, as well as an array of other paradigms such as learning by observation or by instruction. Although there is some overlap between the neuroscience and ANN usage of the term learning, in some cases the terms differ enough to lead to confusion.

Perhaps the greatest divergence in usage is the application of the term “supervised learning.” Supervised learning is central to the many successful recent applications of ANNs to real-world problems of interest. For example, supervised learning is the paradigm that allows ANNs to categorize images accurately. However, to ensure generalization, training such networks requires enormous data sets; one visual query system was trained on more than 107 “labeled” examples (question-answer pairs).

Although the final result of this training is an ANN with a capability that, superficially at least, mimics the human ability to function effectively at (or soon after) birth, what is the challenge faced by this hypothetical algorithm is even greater than it appears. Humans are an outlier: We spend more time learning than perhaps any other animal, in the sense that we have an extended period of immaturity. Many animals function effectively after 106, 105, or even fewer seconds of life: A squirrel can jump from tree to tree within months of birth, a colt can walk within hours, and spiders are born ready to hunt. Examples like these suggest that the challenge may exceed the capacities of even the cleverest unsupervised algorithms.

NATURE COMMUNICATIONS | (2019) 10:3770 | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications
---

PERSPECTIVE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6


alternative? The answer is that much of our sensory representa-

tions and behavior are largely innate. For example, many olfac-

tory stimuli are innately attractive or appetitive (blood for a

shark20 or aversive (fox urine for a rat21). Responses to visual

stimuli can also be innate. For example, mice respond defensively

to looming stimuli, which may allow for the rapid detection and

avoidance of aerial predators22. But the role of innate mechan-

isms goes beyond simply establishing responses to sensory

representations. Indeed, most of the behavioral repertoire of

insects and other short-lived animals is innate. There are also

many examples of complex innate behaviors in vertebrates, for

example in courtship rituals23. A striking example of a complex

innate behavior in mammals is burrowing: Closely related species

of deer mice differ dramatically in the burrows they build with

respect to the length and complexity of the tunnels24,25. These

innate tendencies are independent of parenting: Mice of one

species reared by foster mothers of the other species build bur-

rows like those of their biological parents. Thus, it appears that a

large component of an animal’s behavioral repertoire is not the

result of clever learning algorithms—supervised or unsupervised

but rather of behavior programs already present at birth.

From an evolutionary point of view, it is clear why innate

behaviors are advantageous. The survival of an animal requires

that it solve the so-called “four Fs”—feeding, fighting, fleeing, and

mating—repeatedly, with perhaps only minor tweaks. Each

individual is born, and has a very limited time—from a few days

to a few years—to figure out how to solve these four problems. If

it succeeds, it passes along part of its solution (i.e., half its gen-

ome) to the next generation. Consider a species X that achieves at

98% of its mature performance at birth, and its competitor Y that

functions only at 50% at birth, requiring a month of learning to

achieve mature performance. (Performance here is taken as some

measure of fitness, i.e., ability of an individual to survive and

propagate). All other things being equal (e.g., assuming that

mature performance level is the same for the two species), species

X will outcompete species Y, because of shorter generation times

and because a larger fraction of individuals survive the first

month to reproduce (Fig. 2a).

In general, however, all other things may not be equal. The

mature performance achievable via purely innate mechanisms

might not be the same as that achievable with additional learning

(Fig. 2a). If an environment is changing rapidly—e.g., on the

timescale of a single individual—innate behavioral strategies

might not provide a path to as high a level of mature performance

depicted in Fig. 2b.

| Performance       | Performance       |
| ----------------- | ----------------- |
| Strongly innate   | Strongly innate   |
| Innate + learning | Innate + learning |
| Time after birth  | Time after birth  |

Genomes specify rules for brain wiring

We have argued that the main reason that animals function so

well so soon after birth is that they rely heavily on innate

mechanisms. Innate mechanisms, rather than heretofore undis-

covered unsupervised learning algorithms, provide the base for

Nature’s secret sauce. These innate mechanisms are encoded in

the genome. Specifically, the genome encodes blueprints for

wiring up their nervous system, where by wiring we refer to both

the specification of which neurons are connected, as well as to the

strengths of those connections. These blueprints have been

selected by evolution over hundreds of millions of years, oper-

ating on countless quadrillions of individuals. The circuits spe-

cified by these blueprints provide the scaffolding for innate

behaviors, as well as for any learning that occurs during an ani-

mal’s lifetime.

If the secret sauce is in our genomes, then we must ask what

exactly our genomes specify about wiring. In some simple

organisms, genomes have the capacity to specify every connection

between every neuron, to the minutest detail. The simple worm c.

elegans, for example, has 302 neurons and about 7000 synapses;
---
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6

# PERSPECTIVE

in each individual of an inbred strain, the wiring pattern is largely the same31. So, at one extreme, the genome can encode a lookup table, which is then transformed by developmental processes into a circuit with precise and largely stereotyped connections. But in larger brains, such as those of mammals, synaptic connections cannot be specified so precisely; the genome simply does not have sufficient capacity to specify every connection explicitly. The human genome has about 3 × 109 nucleotides, so it can encode no more than about 1 GB of information—an hour or so of streaming video32. But the human brain has about 1011 neurons, and more than 103 synapses per neuron. Since specifying a connection target requires about log21011 = 37 bits/synapse, it would take about 3.7 × 1015 bits to specify all 1014 connections. (This may represent an under-estimate because it considers only the presence or absence of a connection; a few extra bits/synapse would be required to specify graded synaptic strengths. But because of synaptic noise and for other reasons, synaptic strength may not be specified very precisely. So, in large and sparsely connected brains, most of the information is probably needed to specify the locations of the nonzero elements of the connection matrix rather than their precise value.) Thus, even if every nucleotide of the human genome were devoted to efficiently specifying brain connections, the information capacity would still be at least six orders of magnitude too small.

These fundamental considerations explain why in most brains, the genome cannot specify the explicit wiring diagram, but must instead specify a set of rules for wiring up the brain during development. Even a short set of rules can readily specify the wiring of a very large number of neurons; in the limit, a nervous system wired up like a grid would require only the single rule that each neuron connect to its four nearest neighbors (although such a nervous system would probably not be very interesting). The size of the human genome is about average for mammals, but dwarfed in size by that of many fish and amphibians; the lungfish of the marbled genome is more than 40 times larger than that of humans38. The fact that the human genome could potentially have been much larger suggests that the regularizing effect imposed by the limited capacity of the genome might represent a feature rather than a bug.

# Implications for ANNs

# Supervised learning or supervised evolution?

As noted above, the term “learning” is used differently in ANNs and neuroscience. At the most abstract level, learning can be defined as the process of encoding statistical regularities from the outside world into the parameters (mostly connection weights) of the network. But in the context of animal learning, the source of the input data for learning is limited only to the animal’s “experience,” i.e., to those events that occur during the animal’s lifetime. Wiring rules encoded in the genome that do not depend on experience, such as those used to wire up the retina, are not usually termed “learning.” Because the terms “lifetime” and “experience” are not well defined when applied to an ANN, reconciling the two definitions of learning in ANNs vs. neuroscience poses a challenge.

If, as we have argued above, much of an animal’s behavior is innate, then an animal’s life experiences represent only a small fraction of the data that contribute to its fitness; another potentially much larger pool of data contributes to its innate behaviors and representations. These innate behaviors and representations arise through evolution by natural selection. Thus evolution, like learning, can also be viewed as a mechanism for extracting statistical regularities, albeit on a much longer time scale than learning. Evolution can be thought of as a kind of reinforcement algorithm, operating on the timescale of generations, where the connections pre-trained in the solution to one task are transferred to accelerate learning on a related task42,43.

NATURE COMMUNICATIONS | (2019) 10:3770  | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications
---
PERSPECTIVE
NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6

For example, a network trained to classify objects such as elephants and giraffes might be used as a starting point for a network that distinguishes trees or cars. However, transfer learning differs from the innate mechanisms used in brains in an important way. Whereas in transfer learning the ANN’s entire connection matrix (or a significant fraction of it) is typically used as a starting point, in animal brains the amount of information “transferred” from generation to generation is smaller, because it must pass through the bottleneck of the genome. Passing the information through the genomic bottleneck may select for wiring and plasticity rules which are more generic, and which therefore are more likely to generalize well. For example, the wiring of the visual cortex is quite similar to that of the auditory cortex (although each area has idiosyncrasies). This suggests that the hypothesized canonical cortical circuit provides, with perhaps only minor variations, a foundation for the wide variety of tasks that mammals perform. Neuroscience suggests that there may exist more powerful mechanisms—a kind of generalization of transfer learning—which operate not only within a single sensory modality like vision, but across sensory modalities and even beyond.

A second observation from neuroscience follows from the fact that the genome doesn’t encode representations or behaviors directly or optimization principles directly. The genome encodes wiring rules and patterns, which then must instantiate behaviors and representations. It is these wiring rules that are the target of evolution. This suggests wiring topology and network architecture as a target for optimization in artificial systems. Classical ANNs largely ignored the details of network architecture, guided perhaps by theoretical results on the universality of fully connected three-layer networks. But of course, one of the major advances in the modern era of ANNs has been convolutional neural networks (CNNs), which use highly constrained wiring to exploit the fact that the visual world is translation invariant. The inspiration for this revolutionary technology was in part the structure of visual receptive fields. This is the kind of innate constraint that in animals would be expected to arise through evolution; there might be many others yet to be discovered. Other constraints on wiring and learning rules are sometimes imposed in ANNs through hyperparameters, and there is an extensive literature on hyperparameter optimization. At present, however, ANNs exploit only a tiny fraction of possible network architectures, raising the possibility that more powerful, cortically-inspired architectures remain to be discovered.

In principle, the circuits underlying neural processing could be discovered by experimental neuroscience. Traditionally, neural representations and wiring were inferred indirectly, through recordings of activity. More recently, tools have been developed that raise the possibility of determining wiring motifs and circuitry directly. Local circuitry can be determined with serial electron microscopy; there is now an ambitious project to determine every synapse within a 1 mm3 cube of mouse visual cortex. Long-range projections can be determined in a high-throughput manner using MAPseq or by other methods. Thus the details of cortical wiring may soon be available, and provide an experimental basis for ANNs.

# Conclusions

The notion that the brain provides insights for AI is at the very foundation of ANN research. ANNs represented an attempt to capture some key aspects of the nervous system: many simple units, connected by synapses, operating in parallel. Several subsequent advances also arose from neuroscience. For example, the reinforcement learning algorithms underlying recent successes such as AlphaGo Zero draw their inspiration from the study of animal learning.

Received: 22 June 2019 Accepted: 5 August 2019 Published online: 21 August 2019

# References

1. LeCun, Y., Bengio, Y. &#x26; Hinton, G. Deep learning. Nature 521, 436 (2015).
2. Kurzweil, R. The Singularity is Near. (Gerald Duckworth &#x26; Co, 2010).
3. Moravec, H. Mind Children: The Future of Robot and Human Intelligence. (Harvard University Press, 1988).
4. Kaas, J. H. Neocortex in early mammals and its subsequent variations. Ann. N. Y. Acad. Sci. 1225, 28–36 (2011).
5. Hassabis, D., Kumaran, D., Summerfield, C. &#x26; Botvinick, M. Neuroscience-inspired artificial intelligence. Neuron 95, 245–258 (2017).
6. Seung, S. Connectome: How the Brain’s Wiring Makes Us Who We Are. (HMH, 2012).
7. Locke, J. An essay concerning human understanding: and a treatise on the conduct of the understanding. Complete in one volume with the author as last additions and corrections (Hayes &#x26; Zell, 1860).
8. Kant, I. Critique of Pure Reason. (Cambridge University Press, 1998).
9. Tenenbaum, J. B., Kemp, C., Griffiths, T. L. &#x26; Goodman, N. D. How to grow a mind: statistics, structure, and abstraction. Science 331, 1279–1285 (2011).
10. Haugeland, J. Artificial Intelligence: The Very Idea. (MIT Press, 1989).
11. Rumelhart, D. E. Parallel distributed processing: explorations in the microstructure of cognition. Learn. Intern. Represent. Error Propag. 1, 318–362 (1986).
12. Cybenko, G. Approximation by superpositions of a sigmoidal function. Math. Control, Signals Syst. 2, 303–314 (1989).
13. Hornik, K. Approximation capabilities of multilayer feedforward networks. Neural Netw. 4, 251–257 (1991).
14. Lee, S. Amazing Spiderman (1962).
15. Antolet, S. et al. Vqa: Visual question answering. In Proceedings of the IEEE International Conference on Computer Vision, 2425–2433 (2015).
16. Bell, A. J. &#x26; Sejnowski, T. J. The “independent components” of natural scenes are edge filters. Vis. Res. 37, 3327–3338 (1997).
17. Olshausen, B. A. &#x26; Field, D. J. Emergence of simple-cell receptive field properties by learning a sparse code for natural images. Nature 381, 607 (1996).
18. van Hateren, J. H. &#x26; Ruderman, D. L. Independent component analysis of natural image sequences yields spatio-temporal filters similar to simple cells in primary visual cortex. Proc. R. Soc. Lond. Ser. B: Biol. Sci. 265, 2315–2320 (1998).
19. Wolpert, D. H. The lack of a priori distinctions between learning algorithms. Neural Comput. 8, 1341–1390 (1996).
20. Yopak, K. E., Lisney, T. J. &#x26; Collin, S. P. Not all sharks are “swimming noses”: variation in olfactory bulb size in cartilaginous fishes. Brain Struct. Funct. 220, 1127–1143 (2015).
21. Apfelbach, R., Blanchard, C. D., Blanchard, R. J., Hayes, R. A. &#x26; McGregor, I. S. The effects of predator odors in mammalian prey species: a review of field and laboratory studies. Neurosci. Biobehav. Rev. 29, 1123–1144 (2005).

NATURE COMMUNICATIONS | (2019) 10:3770  | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications
---

NATURE COMMUNICATIONS | https://doi.org/10.1038/s41467-019-11786-6


# PERSPECTIVE

1. Yilmaz, M. &#x26; Meister, M. Rapid innate defensive responses of mice to looming visual stimuli. Curr. Biol. 23, 2011–2015 (2013).
2. Tinbergen, N. The study of instinct. (Clarendon Press/Oxford University Press, Oxford, 1951). Link
3. Weber, J. N. &#x26; Hoekstra, H. E. The evolution of burrowing behaviour in deer mice (genus peromyscus). Anim. Behav. 77, 603–609 (2009).
4. Metz, H. C., Bedford, N. L., Pan, Y. L. &#x26; Hoekstra, H. E. Evolution and genetics of precocious burrowing behavior in peromyscus mice. Curr. Biol. 27, 3837–3845 (2017).
5. Langston, R. F. et al. Development of the spatial representation system in the rat. Science 328, 1576–1580 (2010).
6. McKone, E., Crookes, K. &#x26; Kanwisher, N. et al. The cognitive and neural development of face recognition in humans. Cogn. Neurosci. 4, 467–482 (2009).
7. Kanwisher, N. &#x26; Yovel, G. The fusiform face area: a cortical region specialized for the perception of faces. Philos. Trans. R. Soc. B: Biol. Sci. 361, 2109–2128 (2006).
8. Pinker, S. The Language Instinct. (William Morrow &#x26; co, New York, NY, US, 1994).
9. Marcus, G. F. The birth of the mind: How a tiny number of genes creates the complexities of human thought. (Basic Civitas Books, 2004).
10. Chen, B. L., Hall, D. H. &#x26; Chklovskii, D. B. Wiring optimization can relate neuronal structure and function. Proc. Natl Acad. Sci. USA 103, 4723–4728 (2006).
11. Wei, Y., Tsigankov, D. &#x26; Koulakov, A. The molecular basis for the development of neural maps. Ann. N. Y. Acad. Sci. 1305, 44–60 (2013).
12. Silver, D. et al. A general reinforcement learning algorithm that masters chess, shogi, and go through self-play. Science 362, 1140–1144 (2018).
13. Douglas, R. J., Martin, K. A. C. &#x26; Whitteridge, D. A canonical microcircuit for neocortex. Neural Comput. 1, 480–488 (1989).
14. Harris, K. D. &#x26; Shepherd, G. M. G. The neocortical circuit: themes and variations. Nat. Neurosci. 18, 170 (2015).
15. Poggio, T., Torre, V. &#x26; Koch, C. Computational vision and regularization theory. Nature 317, 314–9 (1985).
16. Tishby, N., Pereira, F. &#x26; Bialek, W. The information bottleneck method. arXiv, (2000).
17. Leitch, I. J. Genome sizes through the ages. Heredity. 99, 121–2 (2007).
18. Andrychowicz, M. et al. Learning to learn by gradient descent by gradient descent. Advances in Neural Information Processing Systems 29. Lee, D. D., Sugiyama M., Luxburg U. V., Guyon I., &#x26; R. Garnett. (eds) 3981–3989 (Curran Associates, Inc., 2016). Link
19. Finn, C., Abbeel, P. &#x26; Levine, S. Model-agnostic meta-learning for fast adaptation of deep networks. In Proceedings of the 34th International Conference on Machine Learning. Vol. 70, 11261135, JMLR. org, (2017).
20. Bellec, G., Salaj, D. Subramoney, A., Legenstein, R. &#x26; Maass, W. Long short-term memory and learning-to-learn in networks of spiking neurons. Adv. Neural Info. Process. Syst. 795805 (2018).
21. Pan, S. J. &#x26; Yang, Q. A survey on transfer learning. IEEE Trans. Knowl. data Eng. 22, 1345–1359 (2010).
22. Vanschoren, J. Meta-learning: a survey. arXiv (2018).
23. Oviedo, H. V., Bureau, I., Svoboda, K. &#x26; Zador, A. M. The functional asymmetry of auditory cortex is reflected in the organization of local cortical circuits. Nat. Neurosci. 13, 1413 (2010).

# Acknowledgements

We thank Adam Kepecs, Alex Koulakov, Alex Vaughan, Barak Pearlmutter, Blake Richards, Dan Ruderman, Daphne Bavelier, David Markowitz, Josh Dubnau, Konrad Koerding, Mike Deweese, Peter Dayan, Petr Znamenskiy, and Ryan Fong for many thoughtful comments on and discussions about earlier versions of this manuscript.

# Additional information

Competing interests: The author declares no competing interests.

Reprints and permission information is available online at http://npg.nature.com/reprintsandpermissions/

Peer review information: Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this work.

Publisher’s note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.


© The Author(s) 2019
NATURE COMMUNICATIONS | (2019) 10:3770  | https://doi.org/10.1038/s41467-019-11786-6 | www.nature.com/naturecommunications
