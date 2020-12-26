<h2 id="tldr">Tl;dr</h2>

* Connectomics is a relatively new field combining neuroscience, microscopy, biology and computer science.

* The goal is to generate maps of the brain at synaptic resolution. By doing so,
  it will hopefully lead to a better understanding of how things work and
  subsequently advance medical approaches to various diseases.

* The datasets required to produce these brain maps are massive since they have
  to be imaged at such a high resolution.

* Manually reconstructing wiring diagrams in the datasets is extremely time consuming and
  expensive so there is a great need to automate the process.

* Reconstructing neurons is challenging because many consecutively correct decisions must be made. Errors can propagate throughout a dataset easily.

* Methods need to also be computationally efficient and scalable to account
  for the size of the data.

* We present a novel approach to neuron segmentation, Local Shape Descriptors
  (LSDs) - a 10-Dimensional embedding used as an auxiliary learning objective
  for boundary detection.

* We find that the LSDs help improve boundaries and subsequent neuron
  reconstructions in several large and diverse datasets.

* They are also two orders of magnitude faster than the current state of the art
  approach.
