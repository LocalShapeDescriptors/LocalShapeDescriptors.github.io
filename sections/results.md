<h2 id="results">Results</h2>

We conducted a large scale study comparing LSD-based methods against three
previous affinity-based methods: (1) direct neighbor and (2) long-range
affinities with mean squared error (MSE) loss, and (3) direct neighbor
affinities with MALIS loss. We also include comparisons against single FFN
segmentations<dt-cite key="januszewski_high-precision_2018"></dt-cite>. The LSD
architectures are described <a href="#network_architectures">here</a>. For a
more detailed overview, see section 3.1 in the paper.

<h3 id="metrics">Metrics</h3>

One challenge of neuron segmentation is finding an evaluation metric which
accurately reflects the quality of a reconstruction. We used two established
metrics: Variation of Information (VoI) and Expected Run-Length (ERL). We also
propose a new metric, which we call the Min-Cut Metric (MCM).

**Variation of Information (VoI)<dt-cite key="meila_comparing_2007"></dt-cite>** - An established metric which measures the amount of over-segmentation (false
  splits) and under-segmentation (false merges) between a proposed segmentation
  and ground truth. Taken together, they constitute the VoI Sum. The goal is to
  minimize the VoI; a perfect score would be zero, meaning a segmentation
  differs as little as possible from the ground truth.

**Expected Run Length (ERL)<dt-cite
key="januszewski_high-precision_2018"></dt-cite>** - A relatively new metric
which measures the expected length of an error-free path along neurons in a
volume. It is an appealing metric to both engineers and neuroscientists since it
relates segmentation errors to neuron cable length.

**Min-Cut Metric (MCM)** - We propose a new metric designed to emulate a human
annotator splitting and merging objects in a segmentation. Specifically, it
gives an approximation of how many clicks are needed to get from a
reconstruction to the correct ground truth (assuming ground truth in
the form of skeletons is available). In a simple case
we have two ground truth skeletons contained inside a falsely merged segment
(1). We perform a min-cut (2), and separate the falsely merged segment into two segments (3).

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/mcm_easy_case.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
  </div>
  </body>
</html>

In a more complex case (1), a min-cut (2) splits the segment but one of the
resulting segments still contains a false merge (3). Another min-cut is
performed (4), resulting in three segments (5). This process is described in
detail in Supplementary section B of the paper.

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/mcm_complex_case.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
  </div>
  </body>
</html>

<h3 id="datasets">Datasets</h3>

We used three large and diverse EM datasets to evaluate all methods and compare
metrics.

**Zebrafinch:** The main component of the study was a region taken from songbird
neural tissue <dt-cite key="januszewski_high-precision_2018"></dt-cite>. The
volume comprises ~10<sup>6</sup> cubic microns of raw data. It was imaged using
SBFEM at 9x9x20 (xyx) nanometer resolution. 0.02% of the data was using for
training (33 volumes containing ~200 cubic microns of labeled neurons). 12
manually traced skeletons (13.5 millimeters) were used for network validation
and 50 skeletons (97 millimeters) were used for evaluation. See below for a
visualization:

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/zfinch_dataset.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
  </div>
  </body>
</html>

After training, we predicted in a slightly smaller testing region (~800,000
cubic microns) which we refer to as the Benchmark ROI (region of interest). We created two sets of
supervoxels, one without any masking, and one constrained to a neuropil mask.


<html>
  <body>
  <div class="accordion-container">
  <nav class="accordion arrows">
  <input type="radio" name="accordion" id="zfinch" />
  <section class="box">
  <label class="box-title" for="zfinch">Zebrafinch</label>
  <label class="box-close" for="acc-close"></label>
  <div class="box-content"><div class="responsive-container">
    <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B2e-8%2C%22m%22%5D%2C%22y%22:%5B2e-8%2C%22m%22%5D%2C%22z%22:%5B2e-8%2C%22m%22%5D%7D%2C%22position%22:%5B2522.154052734375%2C2508.88134765625%2C2990.42919921875%5D%2C%22crossSectionScale%22:16.860758498545437%2C%22projectionOrientation%22:%5B-0.183084174990654%2C-0.3018076419830322%2C0.007873492315411568%2C0.935590922832489%5D%2C%22projectionScale%22:8192%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://j0126-nature-methods-data/GgwKmcKgrcoNxJccKuGIzRnQqfit9hnfK1ctZzNbnuU/rawdata_realigned%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#ff00f7%22%2C%22name%22:%22rawdata_realigned%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22precomputed://gs://j0126-nature-methods-data/GgwKmcKgrcoNxJccKuGIzRnQqfit9hnfK1ctZzNbnuU/tissue_classification%22%2C%22transform%22:%7B%22outputDimensions%22:%7B%22x%22:%5B2e-8%2C%22m%22%5D%2C%22y%22:%5B2e-8%2C%22m%22%5D%2C%22z%22:%5B2e-8%2C%22m%22%5D%2C%22c%27%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22annotations%22%2C%22localDimensions%22:%7B%22c%27%22:%5B1%2C%22%22%5D%7D%2C%22localPosition%22:%5B4%5D%2C%22annotationColor%22:%22#d400ff%22%2C%22shader%22:%22#uicontrol%20vec3%20color%20color%28default=%5C%22magenta%5C%22%29%5Cnvoid%20main%28%29%20%7B%5Cn%20%20emitRGBA%28vec4%28color%2C%20toNormalized%28getDataValue%28%29%29%29%29%3B%5Cn%7D%5Cn%22%2C%22shaderControls%22:%7B%22color%22:%22#0088ff%22%7D%2C%22name%22:%22neuropil%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22neuropil%22%2C%22size%22:649%7D%2C%22layout%22:%224panel%22%7D" "></iframe>
  </div>
  </div>
  </section>
  <input type="radio" name="accordion" id="acc-close" />
  </nav>
  </div>
  </body>
</html>

For each affinity-based network, we created segmentations over a range of ROIs in order to assess performance with scale. We then evaluated VoI, ERL, and MCM.

**Hemi-Brain:** A volume taken from the *Drosophila melanogaster* central brain
<dt-cite key="scheffer_connectome_2020"></dt-cite>. It was imaged with FIBSEM at
8 nanometer isotropic resolution and contains a total of 26 teravoxels of image
data. We restricted experiments to the Ellipsoid Body, a neuropil implicated in
spatial navigation <dt-cite key="turner-evans_insect_2016"></dt-cite>. 0.002% of
the data was used for training (~450 cubic microns of labeled neurons). We
restricted segmentations to three ROIs and evaluated against a filtered list of
neurons traced to completion (voxel-based rather than skeletons).

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/hemi_dataset.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
  </div>
  </body>
</html>

<html>
  <body>
  <div class="accordion-container">
  <nav class="accordion arrows">
  <input type="radio" name="accordion" id="hemi" />
  <section class="box">
  <label class="box-title" for="hemi">Hemi-brain</label>
  <label class="box-close" for="acc-close"></label>
  <div class="box-content"><div class="responsive-container">
    <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B8e-9%2C%22m%22%5D%7D%2C%22position%22:%5B25962.435546875%2C25359.71484375%2C20296.431640625%5D%2C%22crossSectionScale%22:47.72354919422505%2C%22crossSectionDepth%22:-37.62185354999912%2C%22projectionOrientation%22:%5B-0.008687195368111134%2C-0.7010441422462463%2C-0.7130189538002014%2C-0.008097930811345577%5D%2C%22projectionScale%22:21207.72950167948%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-janelia-flyem-hemibrain/emdata/clahe_yz/jpeg%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#0091ff%22%2C%22name%22:%22emdata%22%7D%2C%7B%22type%22:%22segmentation%22%2C%22source%22:%7B%22url%22:%22precomputed://gs://neuroglancer-janelia-flyem-hemibrain/v1.0/rois%22%2C%22subsources%22:%7B%22default%22:true%2C%22properties%22:true%2C%22mesh%22:true%7D%2C%22enableDefaultSubsources%22:false%7D%2C%22pick%22:false%2C%22selectedAlpha%22:0.44%2C%22ignoreNullVisibleSet%22:false%2C%22meshSilhouetteRendering%22:1%2C%22colorSeed%22:2359850678%2C%22segments%22:%5B%2217%22%5D%2C%22segmentQuery%22:%22EB%22%2C%22name%22:%22roi%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22roi%22%2C%22size%22:290%7D%2C%22layout%22:%224panel%22%7D" "></iframe>
  </div>
  </div>
  </section>
  <input type="radio" name="accordion" id="acc-close" />
  </nav>
  </div>
  </body>
</html>

**FIB-25:** An older dataset taken from the *Drosophila* visual system <dt-cite
key="takemura_synaptic_2015"></dt-cite>. It contains ~346 gigavoxels of raw EM
data and was imaged with FIBSEM at 8 nanometer resolution. Four volumes
containing ~160 cubic microns of labeled data were used for training. We
predicted inside the entire volume and then restricted supervoxels to an
irregularly shaped neuropil mask. Segmentations were evaluated inside a 13.6
gigavoxel region contained in the bottom half of the full ROI. Similar to the
Hemi-brain, evaluations were done using a filtered list of completely traced
neurons.

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/fib25_dataset.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
  </div>
  </body>
</html>

<html>
  <body>
  <div class="accordion-container">
  <nav class="accordion arrows">
  <input type="radio" name="accordion" id="fib25" />
  <section class="box">
  <label class="box-title" for="fib25">FIB-25</label>
  <label class="box-close" for="acc-close"></label>
  <div class="box-content"><div class="responsive-container">
    <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B8e-9%2C%22m%22%5D%7D%2C%22position%22:%5B3425.203857421875%2C2993.146240234375%2C3936.575927734375%5D%2C%22crossSectionScale%22:29.90334336415725%2C%22projectionOrientation%22:%5B-0.09087008237838745%2C0.8137544393539429%2C-0.4936932325363159%2C0.292939156293869%5D%2C%22projectionScale%22:11797.675238192334%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-public-data/flyem_fib-25/image%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#007bff%22%2C%22name%22:%22image%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22image%22%7D%2C%22layout%22:%224panel%22%7D" "></iframe>
  </div>
  </div>
  </section>
  <input type="radio" name="accordion" id="acc-close" />
  </nav>
  </div>
  </body>
</html>


<h3 id="accuracy">Accuracy</h3>




<h3 id="throughput">Throughput</h3>

<html>
  <body>
  <div class="accordion-container">
  <nav class="accordion arrows">
  <input type="radio" name="accordion" id="block" />
  <section class="box">
  <label class="box-title" for="block">Block-wise processing overview</label>
  <label class="box-close" for="acc-close"></label>

  <div class="box-content"><div>
  <p>Blockwise processing is necessary to process
  such large volumes in a reasonable amount of time. The idea is to chunk up a
  dataset into small blocks which easily fit in memory, and then distribute
  these blocks over many workers (GPUs for prediction, CPUs for
  post-processing). A little bit of context is required to read the input data
  necessary to write the output data. Because of this, only blocks that do not
  touch can be processed simultaneously. Once they finish processing, the next
  set of blocks can begin, and so on until all blocks are complete. Consider
  watershed for a single neuron:
  </p>
  </div>

  <div class="box-content"><div style="text-align: center;">
  <img class="b-lazy"
  id="watershed_separate_large"
  src="assets/gifs/watershed_separate.gif" style="display: block; margin: auto; width: 100%;"/>
  </div>

  <div class="box-content"><div style="text-align: center;">
  <img class="b-lazy"
  id="watershed_separate_small"
  src="assets/gifs/watershed_separate_small.gif" style="display: block; margin: auto; width: 100%;"/>
  </div>

  <div class="box-content"><div>
  <p>The blocks are processed in an alternating fashion ensuring that none touch. Piecing it together gives us the fragments required to generate a neuron:  </p>
  </div>

  <div class="box-content"><div style="text-align: center;">
    <img class="b-lazy"
    id="watershed_separate_large"
    src="assets/gifs/watershed_joined.gif" style="display: block; margin: auto; width: 100%;"/>
  </div>

  <div class="box-content"><div>
  <p>The same logic can be used to stitch the fragments together based on
  the underlying affinities. The result is an agglomerated neuron:</p>
  </div>

  <div class="box-content"><div style="text-align: center;">
    <img class="b-lazy"
    src="assets/gifs/agglom_full.gif" style="display: block; margin: auto; width: 100%;"/>
  </div>

  <div class="box-content"><div>
  <p>This just shows what is happening on an example neuron. In reality every
  object inside every block contained in the full volume is processed in
  parallel. The result is a very efficient processing scheme. For example
  predicting ~115,000 blocks distributed over 100 GPUs took under 2 hours to
  complete (~800,000 total cubic microns). </p>
  </div>

  </div>
  </section>
  <input type="radio" name="accordion" id="acc-close" />
  </nav>
  </div>
  </body>
</html>

<script>

if (md.is('iPhone')){
  console.log('foo');
  document.getElementById('watershed_separate_small').style.display = 'none';
}
else {
  console.log('moo');
  document.getElementById('watershed_separate_large').style.display = 'none';
}

</script>


---

