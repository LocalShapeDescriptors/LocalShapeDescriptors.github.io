<h2 id="discussion">Discussion</h2>

We introduce the LSDs as an auxiliary learning task for boundary prediction. In
a large scale study, we show that when compared to affinity-based methods, LSDs
improve neuron segmentations across specimen, resolution, and imaging
techniques. When considering performance on neuropil, LSDs implemented in an
auto-context architecture are competitive with the current state of the art and
two orders of magnitude more efficient.

<!--<h3 id="metric_eval">Metric Evaluation</h3>-->

<!--It is difficult to find a robust metric for assessing the quality of a-->
<!--segmentation - an ideal metric would reflect the amount of time needed to-->
<!--proofread a segmentation. In this study, we evaluated two established metrics-->
<!--(VoI, ERL).-->

<!--While both are useful measures, they each have shortcomings. For example, VoI can-->
<!--be sensitive to slight shifts in boundaries. Additionally, small topological-->
<!--changes sometimes go unnoticed which can be problematic in fine neurites where-->
<!--synapses are often located. Since both neurons and their synaptic connections-->
<!--are required to generate a connectome, it is important to consider these-->
<!--regions. ERL is also insenstive to small topological changes and is-->
<!--disproportionately harsh towards merge errors. This means that it favors methods-->
<!--which split more than they merge. Furthermore, ERL seems to be brittle when-->
<!--evaluating on cropped regions, since the cutting of ground truth skeletons-->
<!--introduces variability.-->

<!--Neither metric directly reflects the labor required to resolve a segmentation,-->
<!--which is arguably the relevant quantity to optimize <dt-cite-->
<!--key="plaza_focused_2016,funke_ted_2017"></dt-cite>. Acknowledging that current-->
<!--proofreading tools <dt-fn> <a class="name" target="_blank" rel="noopener-->
<!--noreferrer"-->
<!--href="https://github.com/seung-lab/PyChunkedGraph">PyChunkedGraph</a>, <a-->
<!--class="name" target="_blank" rel="noopener noreferrer"-->
<!--href="https://github.com/janelia-flyem/NeuTu">NeuTu</a></dt-fn> allow annotators-->
<!--to correct merge errors with a few interactions, we introduced the MCM, a metric-->
<!--which relies on graph cuts to represent the amount of interactions needed to fix-->
<!--a segmentation. Assuming an equal distribution of errors, a metric should-->
<!--demonstrate linear growth with volume size. The MCM shows linear growth but is-->
<!--expensive to compute because of repetitive cuts on massive graphs.-->
<!--Interestingly, we found VoI to show general agreement with MCM suggesting it-->
<!--could be used as a reasonable alternative for evaluating larger datasets.-->

<!--<h3 id="auxiliary_learning">Auxiliary Learning</h3>-->

So why do the LSDs improve segmentations?

We hypothesize that using LSDs as an auxiliary learning task incentivizes the
network to consider higher-level features. Since additional local structure has
to be considered, predicting LSDs is likely a harder task than vanilla boundary
detection. The network is forced to make use of more information in its
receptive field than is required for boundary prediction alone. This forces the
network to correlate boundary prediction to LSD prediction.

While Long range affinities also use auxiliary learning (the extra neighborhood
steps), we found they do not perform as well across the investigated datasets.
This could result from several factors including blind spots (missing
neighborhood steps), masking during training, and the isotropy of the data.

See the paper for further details on auto-context, masking and metrics.

<!--<h3 id="auto_context">Auto-Context</h3>-->

<!--We found that using an auto-context approach produced superior segmentations on-->
<!--larger datasets. To test if this was also the case for vanilla boundary-->
<!--detection, we evaluated an affinity auto-context network and found that it made-->
<!--no significant difference in accuracy:-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="neurons"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/zfinch_auto.png"-->
  <!--style="display: block; margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">Auto-context-->
  <!--comparison. A vanilla auto-context network (dashed green line) does not-->
  <!--improve affinity accuracy (blue line). Using the LSDs in an auto-context setup-->
  <!--(dashed orange line), improves multi-task LSD accuracy (red-->
  <!--line).</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--Predicting affinities from affinities is likely too similar to predicting-->
<!--affinities from raw data. We suspect that the second pass of the network simply-->
<!--copies data from the first pass instead of learning new information. Conversely,-->
<!--predicting affinities from LSDs forces the network to incorporate features from-->
<!--the LSDs in the second pass. This improves the final boundary predictions which-->
<!--results in better segmentations.-->

<!--<h3 id="masking">Masking</h3>-->

<!--A big takeaway we found was how important masking becomes when processing large-->
<!--volumes. For reference, binary masks are often used to ignore certain parts of-->
<!--the data (i.e background, artifacts). When segmenting neurons, networks often-->
<!--fail in areas which do not reflect their accuracy on the target task. For-->
<!--example, objects that are underrepresented in the training data (e.g myelin-->
<!--sheaths), or objects that are much larger than the field of view of a network-->
<!--(e.g cell bodies), can lead to false merges in a segmentation. Evaluating-->
<!--performance on neuropil, should be independent of performance on these types of-->
<!--structures (since these objects can be separately predicted and then later-->
<!--merged with a neuron segmentation). This is not a new strategy; recent work on-->
<!--processing large volumes have also included masking at various points in the-->
<!--pipeline<dt-cite-->
<!--key="januszewski_high-precision_2018,li_automated_2019,dorkenwald_binary_2019,scheffer_connectome_2020"></dt-cite>.-->
<!--What was surprising, however, was the extent of accuracy degradation in the-->
<!--absence of masks when scaling to larger datasets:-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="neurons"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/zfinch_mask_delta_voi.png"-->
  <!--style="display: block; margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">Masking improves-->
  <!--accuracy on the Zebrafinch. As we scale up, the accuracy decreases drastically-->
  <!--without using a neuropil mask (the change in VoI sum gets larger between-->
  <!--non-masked and masked predictions as ROI increases).</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--Aside from using masks during post-processing, masks can also be incorporated-->
<!--directly into training. On the zebrafinch, we found that when masking glia out-->
<!--during training, networks that succeeded in learning to mask these areas out-->
<!--(Baseline, MtLSD, AcLSD, AcrLSD) produced better results than those that did not-->
<!--(MALIS, LR).-->
