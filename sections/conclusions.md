<h2 id="conclusions">Conclusions</h2>

Although the LSDs significantly increase boundary prediction accuracy, it is
unclear whether different shape descriptors could lead to further improvements.
The LSDs we propose were subjectively engineered based on features deemed
important to encode object shape. Future experiments could incorporate different
features or focus on learning an optimal embedding. Additionally, the LSDs are
only implemented as an auxiliary learning task for affinity prediction. An
interesting direction would be to agglomerate directly from the LSDs and remove
the need for affinities entirely.

Aside from aiding boundary detection, LSDs could also be used in other ways. For example, they could be incorporated to provide a secondary source of information for
identifying errors in a segmentation. Specifically, after generating a segmentation, LSDs could be calculated on the
labels and then compared with the initial LSD predictions. The difference
between the two would likely highlight regions containing errors:

<div style="text-align: center;">
  <img class="b-lazy"
    id="error_detection"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/error_detection.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Example predicted LSDs between two neurons (1). If the resulting segmentation is correct (2), segmentation LSDs do not differ from predicted LSDs. If the resulting segmentation is incorrect (3), segmentation LSDs (4) might differ from the predicted LSDs. The difference (5) could expose errors in a segmentation.</figcaption></td>
  </tr></table>
</div>

We've also seen promising results when using the LSDs for other segmentation
problems. For example, LSDs have been successful in generating segmentations of
cell bodies:

<div style="text-align: center;">
  <img class="b-lazy"
    id="zfinch"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/zfinch.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Nuclei segmentation
  on full zebrafish brain<dt-cite key="hildebrand_whole-brain_2017"></dt-cite>.
  Columns from left to right: raw, LSD offset vectors, LSD direction vectors
  (covariance), LSD direction vectors (Pearson’s), size, resulting segmentation.
  Scale bars from top to bottom: ∼ 150μm, 20μm, 5μm.</figcaption></td>
  </tr></table>
</div>

The LSDs also produce nice segmentations on mitochondria:

<div style="text-align: center;">
  <img class="b-lazy"
    id="mito"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/mito.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Mitochondria
  segmentation on cropout from FIB-25. Inset shows LSD predictions and
  corresponding segmentation. Right image shows 3D reconstructions of a random
  sample (n=1000) in predicted ROI. Scale bars from left to right: ∼ 3μm, 750nm,
  4μm.</figcaption></td>
  </tr></table>
</div>

Additionally, LSDs have been used for Golgi apparatus and endoplasmic reticulum
segmentation <dt-cite key="gallusser_2020"></dt-cite>. It is likely that objects
with a blob-like structure such as other organelles and various cell types would
benefit from LSDs. Although originally designed for the goal of neuron
segmentation, it would be exciting to see LSDs extended and applied to other
scientific problems.

---
