<h2 id="methods">Methods</h2>

<h3 id="local_shape_descriptors">Local Shape Descriptors</h3>

The intuition behind LSDs is to improve boundary detection by incorporating
statistics describing the local shape of an object close to a boundary. A
similar technique produced superior results over boundary detection alone
<dt-cite key="bai_deep_2017"></dt-cite>. Given a raw EM dataset and unique
neuron labels, we can compute ground truth LSDs in a local window. Specifically,
for each voxel, we grow a gaussian with a fixed radius and intersect it with the
underlying label. We then calculate the center of mass of the intersected region
and compute several statistics between the given voxel and the center of mass.
This is done for all voxels in the window. Perhaps the most important is the
mean offset to center of mass (shown below). This component ensures that a
smooth gradient is maintained within objects while providing sharp contrasts at
object boundaries.

<div style="text-align: center;">
  <img class="b-lazy"
  id="lsd_schematic"
  src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
  data-src="assets/img/lsd_schematic.jpeg"
  style="margin: auto; width: 100%;"/>
  <img class="b-lazy"
  id="lsd_schematic_vertical"
  src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
  data-src="assets/img/lsd_schematic_vertical.jpeg"
  style="margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
<td width="100%"><figcaption style="text-align: center;">Given raw data and
ground truth labels we can compute ground truth LSDs. The general idea is to
grow a gaussian around each voxel and intersect it with the underlying label.
The center of mass of the intersected region is calculated, and statistics
between the voxel and center of mass are computed. Here we see the first
component of the LSDs, the mean offset to center of mass. At object boundaries,
vectors are sharply contrasted in opposing directions. As we get closer to the
center of objects, the difference between the selected voxel and center of mass
decreases, which results in a smoother gradient.</figcaption></td>
</tr></table>
</div>

Additionally, we calculate two statistics describing the directionality of
neural processes (Covariance and Pearson's correlation coefficient). The former
highlights the orientation of neurons while the latter exposes elongation. The
final component is simply the voxel count inside the intersected region which
translates to the size of the process.

<div style="text-align: center;">
  <img class="b-lazy"
    id="lsd_components_vertical"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/lsd_components_vertical.jpeg"
    style="margin: auto; width: 100%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">The components of the
  LSDs, offset to center of mass ([0:3]), covariance ([3:6]), Pearson's
  correlation coefficient ([6:9]), and voxel count ([9:10]). The covariance
  describes neuron orientation (blue = x direction, green = y direction, red = z
  direction), Pearson's describes elongation (or changes in the orientation),
  and voxel count describes the size of the object (blue = small, red = big)
  </figcaption></td>
  </tr></table>
</div>

<div class="accordion-container" id="gt_lsds_div">
<nav class="accordion arrows">
<input type="radio" name="accordion" id="gt_lsds" />
<section class="box">
<label class="box-title" for="gt_lsds">LSD components</label>
<label class="box-close" for="acc-close"></label>
<div class="box-content"><div class="responsive-container">
  <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%7D%2C%22position%22:%5B98.5%2C98.5%2C98.5%5D%2C%22crossSectionScale%22:1.0456762579315313%2C%22projectionOrientation%22:%5B-0.268303781747818%2C-0.36630383133888245%2C-0.03300556540489197%2C0.8903623819351196%5D%2C%22projectionScale%22:595.714724527316%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/gt_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%280%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%281%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%282%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%5Cn%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B0:3%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/raw%22%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#e100ff%22%2C%22name%22:%22raw%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/gt_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%283%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%284%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%285%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B3:6%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/gt_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%286%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%287%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%288%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B6:9%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/gt_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.8%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20float%20v%20=%20toNormalized%28getDataValue%289%29%29%3B%5Cn%20%20%20%20vec4%20rgba%20=%20vec4%280%2C0%2C0%2C0%29%3B%5Cn%20%20%20%20if%20%28v%20%21=%200.0%29%20%7B%5Cn%20%20%20%20%20%20%20%20rgba%20=%20vec4%28colormapJet%28v%29%2C%201.0%29%3B%5Cn%20%20%20%20%7D%5Cn%20%20%20%20emitRGBA%28rgba%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B9:10%5D%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22LSD%5B9:10%5D%22%2C%22size%22:290%7D%2C%22layout%22:%7B%22type%22:%22row%22%2C%22children%22:%5B%7B%22type%22:%22column%22%2C%22children%22:%5B%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B0:3%5D%22%5D%2C%22layout%22:%22yz%22%7D%2C%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B6:9%5D%22%5D%2C%22layout%22:%22yz%22%7D%5D%7D%2C%7B%22type%22:%22column%22%2C%22children%22:%5B%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B3:6%5D%22%5D%2C%22layout%22:%22yz%22%7D%2C%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B9:10%5D%22%5D%2C%22layout%22:%22yz%22%7D%5D%7D%5D%7D%7D"></iframe>
</div>
</div>
</section>
<input type="radio" name="accordion" id="acc-close" />
</nav>
</div>

<div style="text-align: center;">
  <img class="b-lazy"
    id="3d_lsds_mesh"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/3d_lsds_mesh.jpeg"
    style="display: block; margin: auto; width: 80%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
</div>

<div style="text-align: center;">
  <img class="b-lazy"
    id="3d_lsds_vect"
    src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
    data-src="assets/img/3d_lsds_vect.jpeg"
    style="display: block; margin: auto; width: 80%;"/>
  <table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
  <td width="100%"><figcaption style="text-align: center;">foo</figcaption></td>
  </tr></table>
</div>

<div class="accordion-container" id="meh_div">
<nav class="accordion arrows">
<input type="radio" name="accordion" id="meh" />
<section class="box">
<label class="box-title" for="meh">meh</label>
<label class="box-close" for="acc-close"></label>

<div class="box-content"><div><p>meh</p> </div>

<div class="box-content" id="test_div"> <div class="responsive-container">
  <iframe class="responsive-iframe" src="fib_test.html"></iframe>
</div>
</div>
</section>
<input type="radio" name="accordion" id="acc-close" />
</nav>
</div>

<h3 id="network_architectures">Network Architectures</h3>

We implemented the LSDs using three network architectures. All three networks
use a 3D U-Net <dt-fn>A type of <a class="name" target="_blank" rel="noopener
noreferrer"
href="https://towardsdatascience.com/the-most-intuitive-and-easiest-guide-for-convolutional-neural-network-3607be47480">Convolutional
Neural Network (CNN)</a> which has both a downsampling and upsampling path
(giving it the shape of a "U")</dt-fn></a><dt-cite
key="funke_large_2019"></dt-cite>. The first is a multitask approach (MtLSD) in
which the LSDs are predicted along with affinities in a single pass, which is a
similar approach to the Long Range affinities:

<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/mtlsd.png" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
</tr></table>
</div>

The second two architectures use an auto-context approach. The first pass predicts LSDs directly from raw data:

<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/lsd.png" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
</tr></table>
</div>

The LSD network weights are then used to predict LSDs in a larger region. The
predicted LSDs are fed into a second network (AcLSD) in order to predict
affinities:

<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/aclsd.png" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
</tr></table>
</div>

The other auto-context network (AcrLSD) does the same as AcLSD but also includes
a cropped version of the raw data as input to the network, in addition to the
LSDs:

<div style="text-align: center;">
<img class="b-lazy"
src=data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
data-src="assets/img/acrlsd.png" style="display: block; margin: auto; width: 100%;"/>
<table style="width: 100%;" cellspacing="0" cellpadding="0"><tr>
</tr></table>
</div>

<div class="accordion-container" id="pred_lsds_div">
<nav class="accordion arrows">
<input type="radio" name="accordion" id="pred_lsds" />
<section class="box">
<label class="box-title" for="pred_lsds">Predicted LSDs</label>
<label class="box-close" for="acc-close"></label>
<div class="box-content"><div class="responsive-container">
  <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%7D%2C%22position%22:%5B98.5%2C98.5%2C98.5%5D%2C%22crossSectionScale%22:1.0456762579315313%2C%22projectionOrientation%22:%5B-0.268303781747818%2C-0.36630383133888245%2C-0.03300556540489197%2C0.8903623819351196%5D%2C%22projectionScale%22:595.714724527316%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/pred_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%280%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%281%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%282%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%5Cn%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B0:3%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/raw%22%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#e100ff%22%2C%22name%22:%22raw%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/pred_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%283%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%284%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%285%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B3:6%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/pred_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%286%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%287%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%288%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B6:9%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/pred_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22annotations%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.8%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20float%20v%20=%20toNormalized%28getDataValue%289%29%29%3B%5Cn%20%20%20%20vec4%20rgba%20=%20vec4%280%2C0%2C0%2C0%29%3B%5Cn%20%20%20%20if%20%28v%20%21=%200.0%29%20%7B%5Cn%20%20%20%20%20%20%20%20rgba%20=%20vec4%28colormapJet%28v%29%2C%201.0%29%3B%5Cn%20%20%20%20%7D%5Cn%20%20%20%20emitRGBA%28rgba%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22LSD%5B9:10%5D%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22LSD%5B9:10%5D%22%2C%22size%22:290%7D%2C%22layout%22:%7B%22type%22:%22row%22%2C%22children%22:%5B%7B%22type%22:%22column%22%2C%22children%22:%5B%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B0:3%5D%22%5D%2C%22layout%22:%22yz%22%7D%2C%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B6:9%5D%22%5D%2C%22layout%22:%22yz%22%7D%5D%7D%2C%7B%22type%22:%22column%22%2C%22children%22:%5B%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B3:6%5D%22%5D%2C%22layout%22:%22yz%22%7D%2C%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22LSD%5B9:10%5D%22%5D%2C%22layout%22:%22yz%22%7D%5D%7D%5D%7D%7D"></iframe>
</div>
</div>
</section>
<input type="radio" name="accordion" id="acc-close" />
</nav>
</div>

<div class="accordion-container" id="gt_vs_pred_div">
<nav class="accordion arrows">
<input type="radio" name="accordion" id="gt_vs_pred" />
<section class="box">
<label class="box-title" for="gt_vs_pred">Ground truth vs predicted offset
vectors</label>
<label class="box-close" for="acc-close"></label>
<div class="box-content"><div class="responsive-container">
  <iframe class="responsive-iframe" src="https://neuroglancer-demo.appspot.com/#!%7B%22dimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%7D%2C%22position%22:%5B98.5%2C98.5%2C98.5%5D%2C%22crossSectionScale%22:0.6550553083112535%2C%22projectionOrientation%22:%5B-0.268303781747818%2C-0.36630383133888245%2C-0.03300556540489197%2C0.8903623819351196%5D%2C%22projectionScale%22:595.714724527316%2C%22layers%22:%5B%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/gt_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%280%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%281%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%282%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%5Cn%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22GT%20LSD%5B0:3%5D%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/raw%22%2C%22tab%22:%22source%22%2C%22annotationColor%22:%22#e100ff%22%2C%22name%22:%22raw%22%7D%2C%7B%22type%22:%22image%22%2C%22source%22:%7B%22url%22:%22zarr://https://raw.githubusercontent.com/LocalShapeDescriptors/LocalShapeDescriptors.github.io/draft/assets/zarrs/fib.zarr/pred_lsds_updated%22%2C%22transform%22:%7B%22matrix%22:%5B%5B1%2C0%2C0%2C0%2C52%5D%2C%5B0%2C1%2C0%2C0%2C52%5D%2C%5B0%2C0%2C1%2C0%2C52%5D%2C%5B0%2C0%2C0%2C1%2C0%5D%5D%2C%22outputDimensions%22:%7B%22d0%22:%5B1%2C%22%22%5D%2C%22d1%22:%5B1%2C%22%22%5D%2C%22d2%22:%5B1%2C%22%22%5D%2C%22d3%5E%22:%5B1%2C%22%22%5D%7D%7D%7D%2C%22annotationColor%22:%22#0088ff%22%2C%22opacity%22:0.85%2C%22shader%22:%22void%20main%28%29%20%7B%5Cn%20%20%20%20emitRGB%28%5Cn%20%20%20%20%20%20%20%20vec3%28%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%280%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%281%29%29%2C%5Cn%20%20%20%20%20%20%20%20%20%20%20%20toNormalized%28getDataValue%282%29%29%29%5Cn%20%20%20%20%20%20%20%20%29%3B%5Cn%7D%22%2C%22channelDimensions%22:%7B%22d3%5E%22:%5B1%2C%22%22%5D%7D%2C%22name%22:%22Predicted%20LSD%5B0:3%5D%22%7D%5D%2C%22selectedLayer%22:%7B%22layer%22:%22GT%20LSD%5B0:3%5D%22%2C%22size%22:290%7D%2C%22layout%22:%7B%22type%22:%22row%22%2C%22children%22:%5B%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22GT%20LSD%5B0:3%5D%22%5D%2C%22layout%22:%22yz%22%7D%2C%7B%22type%22:%22viewer%22%2C%22layers%22:%5B%22raw%22%2C%22Predicted%20LSD%5B0:3%5D%22%5D%2C%22layout%22:%22yz%22%7D%5D%7D%7D"></iframe>
</div>
</div>
</section>
<input type="radio" name="accordion" id="acc-close" />
</nav>
</div>

---

