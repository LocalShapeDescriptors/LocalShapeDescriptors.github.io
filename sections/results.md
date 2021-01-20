<h2 id="results">Results</h2>

We conducted a large scale study comparing LSD-based methods against three
previous affinity-based methods: (1) direct neighbor and (2) long-range
affinities with mean squared error (MSE) loss, and (3) direct neighbor
affinities with MALIS loss. We also include comparisons against single FFN
segmentations<dt-cite key="januszewski_high-precision_2018"></dt-cite>. For a
more detailed overview, see section 3.1 in the paper.

<!--<h3 id="metrics">Metrics</h3>-->

<!--One challenge of neuron segmentation is finding an evaluation metric which-->
<!--accurately reflects the quality of a reconstruction. We used two established-->
<!--metrics: Variation of Information (VoI) and Expected Run-Length (ERL). We also-->
<!--propose a new metric, which we call the Min-Cut Metric (MCM).-->

<!--**Variation of Information (VoI)<dt-cite key="meila_comparing_2007"></dt-cite>** - An established metric which measures the amount of over-segmentation (false-->
<!--splits) and under-segmentation (false merges) between a proposed segmentation-->
<!--and ground truth. Taken together, they constitute the VoI Sum. The goal is to-->
<!--**minimize** the VoI; a perfect score would be zero, meaning a segmentation-->
<!--differs as little as possible from the ground truth.-->

<!--**Expected Run Length (ERL)<dt-cite-->
<!--key="januszewski_high-precision_2018"></dt-cite>** - A relatively new metric-->
<!--which measures the expected length of an error-free path along neurons in a-->
<!--volume. It is an appealing metric to both engineers and neuroscientists since it-->
<!--relates segmentation errors to neuron cable length. The goal is to **maximize**-->
<!--the ERL; we want to have as much error free cable length as possible.-->

<!--**Min-Cut Metric (MCM)** - We propose a new metric designed to emulate a human-->
<!--annotator splitting and merging objects in a segmentation. Specifically, it-->
<!--gives an approximation of how many clicks are needed to get from a-->
<!--reconstruction to the correct ground truth (assuming ground truth in the form of-->
<!--skeletons is available). The goal is to **minimize** the MCM; the fewer splits-->
<!--and merges required to fix a segmentation, the better. Consider the following cases:-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="neurons"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/mcm_easy_case.jpeg"-->
  <!--style="display: block; margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
<!--<td width="100%"><figcaption style="text-align: center;">Simple case. Two ground-truth <span style="color:#017100">skeletons</span> are contained inside an erroneously merged <span style="color:#9313C6">segment</span>. Dashed lines represent supervoxel boundaries and the closest skeleton <span style="color:#B51700">nodes</span> need to be split to resolve the merge (1). A <span style="color:#FF9300">min-cut</span> is performed (2), resulting in a new <span style="color:#00A2FF">segment</span> (3). </figcaption></td>-->
  <!--</tr></table>-->
  <!--</div>-->

<!--Sometimes a min-cut can fail to separate all nodes of the merged skeletons with-->
<!--a single cut from two selected nodes. In this case, the procedure is repeated-->
<!--until all skeletons are separated, leading to additional split errors:-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="neurons"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/mcm_complex_case.jpeg"-->
  <!--style="display: block; margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">Complex case. Two-->
  <!--<span style="color:#017100">skeletons</span> are contained in a falsely merged-->
  <!--<span style="color:#9313C6">segment</span> as before (1), but the supervoxels-->
  <!--are more fragmented. A <span style="color:#FF9300">min-cut</span> is performed-->
  <!--(2), resulting in a new <span style="color:#00A2FF">segment</span> (3).-->
  <!--However, two <span style="color:#B51700">nodes</span> contained within the-->
  <!--original <span style="color:#9313C6">segment</span> need to be split. A second-->
  <!--<span style="color:#FF9300">min-cut</span> is performed (4), which produces-->
  <!--another <span style="color:#EF5FA7">segment</span> (5). This results in an-->
  <!--additional split error caused by the original cut.</figcaption></td>-->
  <!--</tr></table>-->
  <!--</div>-->

<h3 id="datasets">Datasets</h3>

We used three large and diverse EM datasets to evaluate all methods and compare
metrics.

The main component of the study was a region taken from songbird
neural tissue <dt-cite key="januszewski_high-precision_2018"></dt-cite>. The
volume comprises ~10<sup>6</sup> cubic microns of raw data. It was imaged using
SBFEM at 9x9x20 (xyx) nanometer resolution. 0.02% of the data was using for
training (33 volumes containing ~200 cubic microns of labeled neurons). 12
manually traced skeletons (13.5 millimeters) were used for network validation
and 50 skeletons (97 millimeters) were used for evaluation:

<div style="text-align: center;">
  <img class="b-lazy"
    id="zfinch_dataset"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/zfinch_dataset_large.jpeg"
    style="margin: auto; width: 100%;"/>
  <img class="b-lazy"
    id="zfinch_dataset_vertical"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/zfinch_dataset_vertical_medium.jpeg"
    style="margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Zebrafinch dataset
  overview. 1. 33 gound truth volumes were used for training. 2. Full raw
  dataset, scale bar = 15 μm. 3. Single section shows ground-truth skeletons,
  zoom in scale bar = 500 nm. 4. Validation skeletons (n=12, 13.5 mm). 5.
  Testing skeletons (n=50, 97mm)</figcaption></td>
  </tr></table>
</div>

After training, we predicted in a slightly smaller testing region (~800,000
cubic microns) which we refer to as the Benchmark ROI (region of interest). We
created two sets of supervoxels, one without any masking, and one constrained to
a neuropil mask. For each affinity-based network, we created segmentations over
a range of ROIs in order to assess performance with scale. We then evaluated
VoI, ERL, and MCM. See the paper for details on the other two datasets.

<!--<div class="accordion-container" id="zfinch_div">-->
<!--<nav class="accordion arrows">-->
<!--<input type="radio" name="accordion" id="zfinch" />-->
<!--<section class="box">-->
<!--<label class="box-title" for="zfinch">Zebrafinch raw data and neuropil mask</label>-->
<!--<label class="box-close" for="acc-close"></label>-->

<!--<div class="box-content"><div><p>The raw data and mask used to restrict-->
<!--predictions to the neuropil (blue). Cell bodies, blood vessels, myelin and-->
<!--background voxels were ignored.</p> </div>-->

<!--<div class="box-content"><div class="responsive-container">-->
  <!--<iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B2e-8%2C%22m%22%5D%2C%22y%22:%5B2e-8%2C%22m%22%5D%2C%22z%22:%5B2e-8%2C%22m%22%5D%7D%2C%22position%22:%5B2522.154052734375%2C2508.88134765625%2C2990.42919921875%5D%2C%22crossSectionScale%22:16.860758498545437%2C%22projectionOrientation%22:%5B-0.183084174990654%2C-0.3018076419830322%2C0.007873492315411568%2C0.935590922832489%5D%2C%22projectionScale%22:8192%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://j0126-nature-methods-data/GgwKmcKgrcoNxJccKuGIzRnQqfit9hnfK1ctZzNbnuU/rawdata_realigned%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#ff00f7%22%2C%22name%22:%22rawdata_realigned%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22precomputed://gs://j0126-nature-methods-data/GgwKmcKgrcoNxJccKuGIzRnQqfit9hnfK1ctZzNbnuU/tissue_classification%22%2C%22transform%22:%7B%22outputDimensions%22:%7B%22x%22:%5B2e-8%2C%22m%22%5D%2C%22y%22:%5B2e-8%2C%22m%22%5D%2C%22z%22:%5B2e-8%2C%22m%22%5D%2C%22c%27%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22annotations%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B4%5D%2C%22annotationColor%22:%22#d400ff%22%2C%22shader%22:%22#uicontrol%20vec3%20color%20color%28default=%5C%22magenta%5C%22%29%5Cnvoid%20main%28%29%20%7B%5Cn%20%20emitRGBA%28vec4%28color%2C%20toNormalized%28getDataValue%28%29%29%29%29%3B%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22color%22:%22#0088ff%22%7D%2C%22name%22:%22neuropil%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22neuropil%22%2C%22size%22:649%7D%2C%22layout%22:%224panel%22%7D"></iframe>-->
<!--</div>-->
<!--</div>-->
<!--</section>-->
<!--<input type="radio" name="accordion" id="acc-close" />-->
<!--</nav>-->
<!--</div>-->

<!--**Hemi-Brain:** A volume taken from the *Drosophila melanogaster* central brain-->
<!--<dt-cite key="scheffer_connectome_2020"></dt-cite>. It was imaged with FIBSEM at-->
<!--8 nanometer isotropic resolution and contains a total of 26 teravoxels of image-->
<!--data. We restricted experiments to the Ellipsoid Body, a neuropil implicated in-->
<!--spatial navigation <dt-cite key="turner-evans_insect_2016"></dt-cite>. 0.002% of-->
<!--the data was used for training (~450 cubic microns of labeled neurons). We-->
<!--restricted segmentations to three ROIs and evaluated against a filtered list of-->
<!--neurons traced to completion (voxel-based rather than skeletons).-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="hemi_dataset"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/hemi_dataset_large.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
<!--<img class="b-lazy"-->
  <!--id="hemi_dataset_vertical"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/hemi_dataset_vertical_medium.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%">-->
  <!--<figcaption-->
  <!--id="hemi_caption"-->
  <!--style="text-align: center;">-->
  <!--Hemi-Brain dataset overview. 1. 8 ground-truth volumes were used for training.-->
  <!--2. Full Hemi-brain volume, scale bar = 30 μm. Experiments were restricted to-->
  <!--Ellipsoid Body (circled region). 3. Volumes used for testing. 4. Example-->
  <!--sparse ground-truth testing data, scale bar = 2.5 μm. 5. Zoom-in, scale bar =-->
  <!--800 nm. 6. Example 3D renderings of selected neurons.-->
  <!--</figcaption>-->
  <!--<figcaption-->
  <!--id="hemi_caption_vertical"-->
  <!--style="text-align: center;">-->
  <!--Hemi-Brain dataset overview.-->
  <!--1. Full Hemi-brain volume, scale bar = 30 μm. Experiments were restricted to-->
   <!--Ellipsoid Body (circled region). 2. 8 ground-truth volumes were used for-->
   <!--training. 3. Volumes used for testing. 4. Example sparse ground-truth-->
   <!--testing data, scale bar = 2.5 μm. 5. Zoom-in, scale bar = 800 nm. 6.-->
   <!--Example 3D renderings of selected neurons.-->
  <!--</figcaption>-->
  <!--</td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--<div class="accordion-container" id="hemi_div">-->
<!--<nav class="accordion arrows">-->
<!--<input type="radio" name="accordion" id="hemi" />-->
<!--<section class="box">-->
<!--<label class="box-title" for="hemi">Hemi-brain and EB mask</label>-->
<!--<label class="box-close" for="acc-close"></label>-->

<!--<div class="box-content"><div class="responsive-container">-->
  <!--<iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B8e-9%2C%22m%22%5D%7D%2C%22position%22:%5B25962.435546875%2C25359.71484375%2C20296.431640625%5D%2C%22crossSectionScale%22:47.72354919422505%2C%22crossSectionDepth%22:-37.62185354999912%2C%22projectionOrientation%22:%5B-0.008687195368111134%2C-0.7010441422462463%2C-0.7130189538002014%2C-0.008097930811345577%5D%2C%22projectionScale%22:21207.72950167948%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-janelia-flyem-hemibrain/emdata/clahe_yz/jpeg%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#0091ff%22%2C%22name%22:%22emdata%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%7B%22url%22:%22precomputed://gs://neuroglancer-janelia-flyem-hemibrain/v1.0/rois%22%2C%22subsources%22:%7B%22default%22:true%2C%22properties%22:true%2C%22mesh%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22pick%22:false%2C%22selectedAlpha%22:0.44%2C%22ignoreNullVisibleSet%22:false%2C%22meshSilhouetteRendering%22:1%2C%22colorSeed%22:2359850678%2C%22segments%22:%5B%2217%22%5D%2C%22segmentQuery%22:%22EB%22%2C%22name%22:%22roi%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22roi%22%2C%22size%22:290%7D%2C%22layout%22:%224panel%22%7D"></iframe>-->
<!--</div>-->
<!--</div>-->
<!--</section>-->
<!--<input type="radio" name="accordion" id="acc-close" />-->
<!--</nav>-->
<!--</div>-->

<!--**FIB-25:** An older dataset taken from the *Drosophila* visual system <dt-cite-->
<!--key="takemura_synaptic_2015"></dt-cite>. It contains ~346 gigavoxels of raw EM-->
<!--data and was imaged with FIBSEM at 8 nanometer resolution. Four volumes-->
<!--containing ~160 cubic microns of labeled data were used for training. We-->
<!--predicted inside the entire volume and then restricted supervoxels to an-->
<!--irregularly shaped neuropil mask. Segmentations were evaluated inside a 13.6-->
<!--gigavoxel region contained in the bottom half of the full ROI. Similar to the-->
<!--Hemi-brain, evaluations were done using a filtered list of completely traced-->
<!--neurons.-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="fib25_dataset"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/fib25_dataset_large.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<img class="b-lazy"-->
  <!--id="fib25_dataset_vertical"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/fib25_dataset_vertical_medium.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">FIB-25 dataset-->
  <!--overview. 1. 4 ground-truth volumes were used for training. 2. Full volume-->
  <!--with cutout showing testing region, scale bar = 5 μm. 3. Cross section with-->
  <!--sparsely labeled testing ground-truth. 4. Zoom-in, scale bar = 750 nm. 5.-->
  <!--Sub-volume corresponding to zoomed-in plane. 6. Subset of full RoI testing-->
  <!--neurons. Small volume shown for context.</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--<div class="accordion-container" id="fib25_div">-->
<!--<nav class="accordion arrows">-->
<!--<input type="radio" name="accordion" id="fib25" />-->
<!--<section class="box">-->
<!--<label class="box-title" for="fib25">FIB-25</label>-->
<!--<label class="box-close" for="acc-close"></label>-->
<!--<div class="box-content"><div class="responsive-container">-->
  <!--<iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B8e-9%2C%22m%22%5D%7D%2C%22position%22:%5B3425.203857421875%2C2993.146240234375%2C3936.575927734375%5D%2C%22crossSectionScale%22:29.90334336415725%2C%22projectionOrientation%22:%5B-0.09087008237838745%2C0.8137544393539429%2C-0.4936932325363159%2C0.292939156293869%5D%2C%22projectionScale%22:11797.675238192334%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-public-data/flyem_fib-25/image%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#007bff%22%2C%22name%22:%22image%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22image%22%7D%2C%22layout%22:%224panel%22%7D"></iframe>-->
<!--</div>-->
<!--</div>-->
<!--</section>-->
<!--<input type="radio" name="accordion" id="acc-close" />-->
<!--</nav>-->
<!--</div>-->

<h3 id="accuracy">Accuracy</h3>

We found that the LSDs are beneficial for improving the accuracy of direct
neighbor affinities and subsequently the resulting neuron segmentations. On the
Zebrafinch dataset, we found that LSD architectures out-perform other
affinity-based networks over a range of ROIs when used in an auto-context
approach. When considering segmentation performance restricted directly to
neuropil, our best auto-context network (AcRLSD) performs on par with the
current state of the art when considering VoI:

<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/zfinch_voi_roi.png"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">VoI Sum vs ROI size.
  Each point corresponds to an ROI size. It is ideal to minimize VoI Sum. As we
  scale up, VoI increases because the number of errors increase. The best LSD
  network (AcRLSD - orange) is competitive with FFN (black).</figcaption></td>
  </tr></table>
</div>

We did not find this to be the case when evaluating ERL, which could be a direct
result of asymmetric contributions of split and merge errors in the metric. ERL
can not exceed the average length of skeletons, and thus the addition of shorter
skeletons fragments can result in a decrease of ERL, even in the absence of
errors. ERL measures do not progress monotonically over RoI sizes and absolute
values are likely not comparable across different dataset sizes:

<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/erl_roi.png"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">ERL (nanometers) vs
  ROI size. As we scale up, we observe varying ERLs across all networks from
  cutting the ground truth skeletons. This makes it hard to deduce network
  accuracy from this metric when evaluating on cropped volumes.
  </figcaption></td>
  </tr></table>
</div>

<!--We designed the MCM to simulate the amount of human interactions (clicks) needed-->
<!--to split and merge neurons in a proposed segmentation. Since repeated min-cuts-->
<!--need to be made on large fragment graphs, the computational costs limited MCM-->
<!--calculations to the three smallest ROIs (the largest being ~16,000 cubic-->
<!--microns). We observed an expected linear increase in MCM with scale (more clicks-->
<!--required to resolve larger volumes). We also found VoI to serve as a reasonable-->
<!--proxy to the MCM, which suggests that VoI is a good metric to compare-->
<!--segmentation quality in the context of a proofreading workflow that allows-->
<!--annotators to split false merges using a min-cut on the fragment graph:-->

<!--<div style="text-align: center;">-->
  <!--<img class="b-lazy"-->
  <!--id="voi_mcm"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/voi_mcm_rois.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<img class="b-lazy"-->
  <!--id="voi_mcm_vertical"-->
  <!--src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==-->
  <!--data-src="assets/img/voi_mcm_rois_vertical.jpeg"-->
  <!--style="margin: auto; width: 80%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">Comparison of VoI and-->
  <!--MCM on first three ROIs (up to ~16k cubic microns). As expected, the number of-->
  <!--splits and merges needed to fix a segmentation increases linearly with scale.-->
  <!--The same network order is seen in VoI, suggesting that it might be a-->
  <!--reasonable to MCM on larger volumes.</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--<div class="accordion-container">-->
<!--<nav class="accordion arrows">-->
<!--<input type="radio" name="accordion" id="fib_results" />-->
<!--<section class="box">-->
<!--<label class="box-title" for="fib_results">Fib Results</label>-->
<!--<label class="box-close" for="acc-close"></label>-->

<!--<div class="box-content"><div>-->
  <!--<p> <b>Hemi-Brain - </b> We evaluated segmentations on three ROIs contained-->
  <!--within the Ellipsoid Body. Since the ground truth data was voxel-based (not-->
  <!--skeletons), we only considered VoI. We found LSD methods out-performed other-->
  <!--affinity-based methods and were on par with FFN. The multitask network-->
  <!--performs well on the smaller two ROIs but shows worse results on the largest-->
  <!--ROI (in comparison to AcLSD & AcrLSD), strengthening the argument for using-->
  <!--auto-context on larger volumes: </p>-->
<!--</div>-->

<!--<div class="box-content"><div style="text-align: center;">-->
  <!--<img-->
  <!--id="hemi_voi"-->
  <!--src="assets/img/hemi_rois.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<img-->
  <!--id="hemi_voi_vertical"-->
  <!--src="assets/img/hemi_rois_vertical.jpeg"-->
  <!--style="margin: auto; width: 70%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">VoI split/merge-->
  <!--curves (lines) across thresholds, for each of the three investigated ROIs.-->
  <!--Points indicate the threshold at which VoI Sum is minimized. LSDs maintain-->
  <!--competitiveness with FFN on larger two ROIs.</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--<div class="box-content"><div>-->
  <!--<p> <b>FIB-25 - </b>Similar to the Hemi-Brain, we only evaluated VoI since the-->
  <!--ground truth was voxel based. On the full testing RoI, we found that only one-->
  <!--LSD method (MtLSD) performed well. Interestingly, the auto-context methods-->
  <!--performed poorly here. Upon visual inspection, we found false merges occurring-->
  <!--outside of the testing RoI. We then cropped two volumes contained entirely-->
  <!--within dense neuropil and found auto-context results to improve, further-->
  <!--highlighting the importance of masking: </p>-->
<!--</div>-->

<!--<div class="box-content"><div style="text-align: center;">-->
  <!--<img-->
  <!--id="fib25_voi"-->
  <!--src="assets/img/fib25_rois.jpeg"-->
  <!--style="margin: auto; width: 100%;"/>-->
  <!--<img-->
  <!--id="fib25_voi_vertical"-->
  <!--src="assets/img/fib25_rois_vertical.jpeg"-->
  <!--style="margin: auto; width: 70%;"/>-->
  <!--<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>-->
  <!--<td width="100%"><figcaption style="text-align: center;">VoI split/merge-->
  <!--curves (lines) across thresholds on investigated ROIs. On the Full ROI,-->
  <!--auto-context methods did not perform well. This was likely caused by-->
  <!--peripheral merges. Evaluation on two sub ROIs showed results consistent with-->
  <!--what was seen on the other datasets.</figcaption></td>-->
  <!--</tr></table>-->
<!--</div>-->

<!--</div>-->
<!--</section>-->
<!--<input type="radio" name="accordion" id="acc-close" />-->
<!--</nav>-->
<!--</div>-->

<h3 id="throughput">Throughput</h3>

As described previously, the acquisition size of datasets is growing rapidly.
Segmentation methods should complement this trajectory by being fast and
computationally inexpensive. When considering computational costs in terms of
floating point operations (FLOPs), we found that our best method (AcrLSD) is two
orders of magnitude more efficient than the current state of the art, while
producing segmentations of comparable quality:

<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/voi_tflops.png"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Accuracy vs
  computational costs. Over a range of ROIs (points) affinity-based methods
  require significantly less teraFLOPs (floating point operations) than FFN.
  Auto-context networks (green/orange) are also accurate enough to make their
  slight computational overhead justifiable.</figcaption></td>
  </tr></table>
</div>

All affinity-based methods can be parallelized efficiently using
a modest amount of GPUs, resulting in higher throughput:

<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/inference_table.png"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Inference costs on
  Zebrafinch benchmark ROI (~800k cubic microns). Predicting LSDs, for example,
  took 2 hours using 100 GPUs.</figcaption></td>
  </tr></table>
</div>

This is accomplished using a block-wise processing scheme in which a large
volume is broken down into smaller chunks. The chunks can then be distributed
over many workers in such a way that ensures non-neighboring blocks are
processed simultaneously. As soon as a worker finishes processing a block it
will start processing another valid block. This repeats until the entire volume
is processed. Consider watershed as an example:

<div style="text-align: center;">
  <img class="b-lazy"
    id="blockwise_image"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/blockwise_processing_large.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">Overview of block-wise
  processing scheme. Example 32 μm RoI showing total block grid (A) and required
  blocks to process example neuron (B). Scale bar = ∼ 6μm. Corrsponding
  orthographic view highlights supervoxels generated during watershed (C). Block
  size = 3.6 μm. Inset shows respective raw data inside single block (scale bar
  = ∼ 1μm). Supervoxels are then agglomerated to obtain a resulting segment (D).
  Note: While this example shows processing of a single neuron, in reality all
  neurons are processed simultaneosuly.</figcaption></td>
  </tr></table>
</div>

Blockwise processing is necessary to process such large volumes in a reasonable
amount of time. A little bit of context is required to read the input data
necessary to write the output data. Because of this, only blocks that do not
touch can be processed simultaneously:

<div style="text-align: center;">
  <img class="b-lazy"
    id="watershed_separate_large"
    src="assets/gifs/watershed_separate_large.gif" style="margin: auto; width: 100%;">
  <img class="b-lazy"
    id="watershed_separate_medium"
    src="assets/gifs/watershed_separate_medium.gif" style="margin: auto; width: 100%;"/>
</div>

The blocks are processed in an alternating fashion ensuring that none touch. Piecing it together gives us the fragments required to generate a neuron:

<div style="text-align: center;">
<img class="b-lazy"
  id="watershed_joined_large"
  src="assets/gifs/watershed_joined_large.gif" style="margin: auto; width: 100%;">
<img class="b-lazy"
  id="watershed_joined_medium"
  src="assets/gifs/watershed_joined_medium.gif" style="margin: auto; width: 100%;"/>
</div>

The same logic can be used to stitch the fragments together based on
the underlying affinities. The result is an agglomerated neuron:

<div style="text-align: center;">
<img class="b-lazy"
  id="agglom_joined_large"
  src="assets/gifs/agglom_joined_large.gif" style="margin: auto; width: 100%;">
<img class="b-lazy"
  id="agglom_joined_medium"
  src="assets/gifs/agglom_joined_medium.gif" style="margin: auto; width: 100%;"/>
</div>

This just shows what is happening on an example neuron. In reality every object
inside every block contained in the full volume is processed in parallel. The
result is a very efficient processing scheme. For example predicting ~115,000
blocks distributed over 100 GPUs took under 2 hours to complete (~800,000 total
cubic microns).

---

