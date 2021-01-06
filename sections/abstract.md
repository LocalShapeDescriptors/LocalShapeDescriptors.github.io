## Abstract

  We present a simple, yet effective, auxiliary learning task for the problem of
  neuron segmentation in electron microscopy volumes. The auxiliary task
  consists of the prediction of Local Shape Descriptors (LSDs), which we combine
  with conventional voxel-wise direct neighbor affinities for neuron boundary
  detection. The shape descriptors are designed to capture local statistics
  about the neuron to be segmented, such as diameter, elongation, and direction.
  On a large study comparing several existing methods across various specimen,
  imaging techniques, and resolutions, we find that auxiliary learning of LSDs
  consistently increases segmentation accuracy of affinity-based methods over a
  range of metrics. Furthermore, the addition of LSDs promotes affinity-based
  segmentation methods to be on par with the current state of the art for neuron
  segmentation (Flood-Filling Networks, FFN), while being two orders of
  magnitudes more efficient - a critical requirement for the processing of
  future petabyte-sized datasets. Implementations of the new auxiliary learning
  task, network architectures, training, prediction, and evaluation code, as
  well as the datasets used in this study are publicly available as a benchmark
  for future method contributions.

---

