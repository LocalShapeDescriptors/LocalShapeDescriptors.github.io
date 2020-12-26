## Abstract

We present a novel approach to neuron segmentation in electron microscopy
volumes, which is based on the prediction of Local Shape Descriptors (LSDs) in
combination with conventional voxel-wise direct neighbor affinities for neuron
boundary detection. The shape descriptors capture local statistics about the
neuron to be segmented, such as diameter, elongation, and direction. We show
that learning to predict LSDs as an auxiliary learning task significantly
improves the accuracy of the predicted affinities and subsequently of the
obtained segmentations. We compare our method in a large comparative study
against several existing methods across various specimen, imaging techniques,
and resolutions. The results demonstrate that auxiliary learning of LSDs
consistently increases segmentation accuracy over a range of metrics on all
investigated datasets, when compared to other affinity-based methods. Notably,
our method is competitive with the current state of the art for neuron
segmentation, albeit two orders of magnitude more efficient—a critical
requirement for the processing of future petabyte-sized datasets. Our method,
together with evaluation code and consolidated evaluation datasets, is publicly
available as a benchmark for future method contributions.

---

