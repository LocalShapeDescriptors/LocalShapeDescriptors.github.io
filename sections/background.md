<h2 id="background">Background</h2>

<h3 id="connectomics">Connectomics</h3>

Connectomics is an emerging field which integrates multiple domains including
neuroscience, microscopy, and computer science. The overarching goal is to
provide insights about the brain at resolutions which are not achievable with
other approaches. The ability to study neural structures at this scale will
hopefully lead to a better understanding of brain disorders, and subsequently
advance medical approaches towards finding treatments & cures.

The basic idea is to produce "connectomes" which are essentially maps of the
brain. These maps, or "wiring diagrams", give scientists the ability to see how
every neuron interacts through synaptic connections. They can be used to
complement existing techniques <dt-cite
key="schlegel_synaptic_2016,turner-evans_neuroanatomical_2020"></dt-cite> and
drive future experiments <dt-cite
key="schneider-mizell_quantitative_2016,motta_dense_2019,bates_complete_2020"></dt-cite>.

Okay, but how are the brain maps generated?

Before generating neural wiring diagrams, we first need to acquire the brain
tissue to use. Currently, only Electron Microscopy (EM) allows imaging of neural
tissue at a resolution sufficient to see individual synapses. After extracting a
brain (for example, from a fruit fly), the tissue is generally stained with
heavy metals to increase contrast between structures of interest (i.e neuron
membranes). Once stained, the tissue is imaged with an electron microscope.
There are a few types of EM imaging approaches. Three popular techniques are
serial section transmission EM (ssTEM), serial block-face scanning EM (SBF-SEM)
and focused ion beam scanning EM (FIB-SEM). The former two methods involve
slicing the brain into super thin (e.g 20 nanometer) sections. The latter uses
an ion beam to erode the tissue. In either case, electrons are shot at the
tissue to produce an image of the data. This is a way oversimplified
explanation, for a better overview of these EM imaging techniques (and others),
see <dt-cite key="briggman_volume_2012"> this paper</dt-cite>, specifically
Figure 1.

Sweet! Let's image a human brain and be done with it.

Unfortunately, by imaging brains at such high resolution, the resulting data is
massive. Let's consider the fruit fly example.  A full adult fruit fly brain
(**FAFB**) imaged with ssTEM <dt-cite key="zheng_complete_2018"></dt-cite> at a
pixel resolution of ~4 nanometers and ~40 nanometer thick sections, comprises
~213 teravoxels of data (~50 teravoxels of actual brain tissue)<dt-cite
key="heinrich_synaptic_2018"></dt-cite>. For reference, a voxel is a volumetric
pixel, and the "tera" prefix means 10<sup>12</sup>. So, one fly brain contains
upwards of 213,000,000,000,000 volumetric pixels. To put that in perspective,
<dt-cite key="abbott_mind_2020">Abbott et al.</dt-cite> argue that, assuming a
scale where 1000 cubic microns is equivalent to 1 centimeter, a fruit fly brain
would comprise the length of 6 and a half Boeing 747 aeroplanes. This still
pales in comparison to a mouse brain which would be the distance from Boston to
Lisbon, and require the acquisition of 1 million terabytes of data.

<html>
  <body>
<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/scale1.jpeg" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
<td width="50%"><figcaption style="text-align: center;">Scale perspective. A
fruit fly brain imaged at synaptic resolution takes up 100's of terabytes of
storage space. It allows us to see fine structures such as neural plasma
membranes (pink arrow), synapses (blue arrow), vesicles (green arrow) and
mitochondria (orange arrow). 3D fruit fly model kindly provided by <a
href="https://scholar.google.com/citations?user=ir1vhA8AAAAJ&hl=en"
target="_blank">Igor Siwanowicz</a></figcaption></td>
</tr></table>
  </div>
  </body>
</html>

Try navigating the fly brain in an interactive <a
href="https://github.com/google/neuroglancer" target="_blank">Neuroglancer</a>
viewer (click question mark for controls). Think, Google Earth for brains:

<html>
  <body>
    <div class="accordion-container">
      <nav class="accordion arrows">
        <input type="radio" name="accordion" id="cb1" checked/>
        <section class="box">
          <label class="box-title" for="cb1">Full adult fly brain interactive viewer</label>
          <label class="box-close" for="acc-open"></label>
          <input type="radio" name="accordion" id="acc-open"/>
          <div class="box-content">
            <div class="responsive-container">
              <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22x%22:%5B8e-9%2C%22m%22%5D%2C%22y%22:%5B8e-9%2C%22m%22%5D%2C%22z%22:%5B4e-8%2C%22m%22%5D%7D%2C%22position%22:%5B63696.5703125%2C30152.005859375%2C3242.8369140625%5D%2C%22crossSectionScale%22:413.08059520030787%2C%22projectionOrientation%22:%5B-0.06840167939662933%2C-0.4631274342536926%2C-0.204045370221138%2C0.8597671985626221%5D%2C%22projectionScale%22:124585.76409043159%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%22precomputed://gs://neuroglancer-fafb-data/fafb_v14/fafb_v14_clahe%22%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#0088ff%22%2C%22name%22:%22fafb_v14_clahe%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22fafb_v14_clahe%22%7D%2C%22layout%22:%224panel%22%2C%22partialViewport%22:%5B0%2C0%2C1%2C1%5D%7D" "></iframe>
            </div>
          </div>
        </section>
      </nav>
    </div>
  </body>
</html>

Okay, now we have the data, so how do we create the wiring diagrams?

To create a wiring diagram, we need to reconstruct all of the neurons and their
synaptic connections. This process can be done manually - which consists of
human annotators navigating these datasets and labeling every neuron and their
synaptic partners using various software <dt-cite
key="saalfeld2009catmaid,boergens_webknossos_2017,berger_vast_2018,zhao_neutu_2018"></dt-cite>.
However, this can become extremely tedious and expensive (**$$$**) given the
size of the datasets. For example, simply reconstructing 129 neurons from
**FAFB** took a team of tracers ~60 days to complete<dt-cite
key="zheng_complete_2018"></dt-cite>. Given that a fruit fly has ~100,000
neurons, purely manual reconstruction of connectomes is obviously infeasible.

Consequently, methods have been developed to automate this process. From here
on, we will focus on the automatic reconstruction of neurons. To see the current
approaches to synapse detection, check <dt-cite
key="kreshuk_who_2015,heinrich_synaptic_2018,huang_fully-automatic_2018,buhmann_automatic_2020">
these papers</dt-cite> out!

<h3 id="neuron_segmentation">Neuron Segmentation</h3>

Neuron segmentation is the current rate-limiting step for generating large
connectomes. Errors in a neuron segmentation can easily propagate throughout a
dataset as the scale increases, which makes it tedious for humans to proofread
the data without advanced tools.

<html>
  <body>
  <div class="accordion-container">
  <nav class="accordion arrows">
  <input type="radio" name="accordion" id="seg" />
  <section class="box">
  <label class="box-title" for="seg">Segmentation overview</label>
  <label class="box-close" for="acc-close"></label>

  <div class="box-content"><div> <p> To better understand the problem of neuron
  segmentation, it is necessary to understand what segmentation is. There are a
  few ways to detect objects in an image. A standard approach is called **object
  detection** which is a technique used to locate and label objects, often
  resulting in fitting a bounding box to each object. This is a good strategy
  for finding and tracking objects in an image but it neglects the volumetric
  data contained within an object. An alternative method is called segmentation
  in which every pixel of an object is assigned to a class. There are two main
  techniques: **semantic segmentation** and **instance segmentation**. In
  semantic segmentation, each pixel is assigned to a broader class, for example
  each car in an image would be assigned to a car class and each animal in an
  image would be assigned to a animal class. Conversely, instance segmentation
  assigns each pixel to a unique label. Consider the following example: each
  shoe in the image can be located (object detection), each pixel of each shoe
  can be assigned to a class indicating the type of shoe (semantic
  segmentation), and each pixel can be assigned a unique label indicating the
  specific shoe: </p> </div>

  <div class="box-content"><div style="text-align: center;">
    <img id="shoes" src="assets/img/detection_vs_segmentation_shoes.jpeg" style="display: block; margin: auto; width: 100%;"/>
  </div>

  <div class="box-content"><div style="text-align: center;">
    <img id="shoes_vertical" src="assets/img/detection_vs_segmentation_shoes_vertical.jpeg" style="display: block; margin: auto; width: 100%;"/>
  </div>

  </div>
  </section>
  <input type="radio" name="accordion" id="acc-close" />
  </nav>
  </div>
  </body>
</html>

Neuron reconstruction is an instance segmentation problem because every pixel of
every neuron needs to be assigned a unique label (in contrast to object
detection and semantic segmentation).

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/detection_vs_segmentation_neurons.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
<table id="neurons_caption" style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
<td width="50%"><figcaption style="text-align: center;">foo</figcaption></td>
</tr></table>
  </div>
  </body>
</html>

<html>
  <body>
<div style="text-align: center;">
  <img class="b-lazy"
    id="neurons_vertical"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/detection_vs_segmentation_neurons_vertical.jpeg"
    style="display: block; margin: auto; width: 100%;"/>
<table id="neurons_caption_vertical" style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
<td width="50%"><figcaption style="text-align: center;">foo</figcaption></td>
</tr></table>
  </div>
  </body>
</html>

It would be ideal to directly predict unique labels (neurons) in a dataset.
Unfortunately this requires global information which is difficult because
neurons span large distances. Due to the nature of neural networks, field of
views are not large enough to account for downstream changes in a neuron such as
branching and merging. Consequently, alternative approaches aim to solve the
problem locally.

<script>

if (md.is('iPhone')){
  console.log('foo');
  document.getElementById('shoes_vertical').style.display = 'none';
  document.getElementById('neurons_vertical').style.display = 'none';
  document.getElementById('neurons_caption_vertical').style.display = 'none';
}
else {
  console.log('moo');
  document.getElementById('shoes').style.display = 'none';
  document.getElementById('neurons').style.display = 'none';
  document.getElementById('neurons_caption').style.display = 'none';
}

</script>

<h3 id="related_work">Related Work</h3>

* boundaries
* affinities
* long range
* malis
* ffn
* metric learning
* watershed / agglom variants

<html>
  <body>
<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/related_methods_vertical.jpeg" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
</tr></table>
  </div>
  </body>
</html>

<h3 id="contributions">Contributions</h3>

* introduce lsds
* large scale study

---
