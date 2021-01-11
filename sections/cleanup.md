<script>

//lazy script to choose images with respect to whether user is using
//phone/tablet (smaller width) or computer (higher width). This should probably be
//changed to use img srcset tags (which is what is used for the lsds header
//image), but it was causing problems for the rest of the images and i couldn't be
//bothered to fix it

//Also need to only show neuroglancer links if on computer - browser needs to be
//chrome (>= 51) or firefox (>= 46).

var md = new MobileDetect(window.navigator.userAgent);

function get_browser() {
    var ua=navigator.userAgent,tem,M=ua.match(/(opera|chrome|safari|firefox|msie|trident(?=\/))\/?\s*(\d+)/i) || []; 
    if(/trident/i.test(M[1])){
        tem=/\brv[ :]+(\d+)/g.exec(ua) || []; 
        return {name:'IE',version:(tem[1]||'')};
        }
    if(M[1]==='Chrome'){
        tem=ua.match(/\bOPR|Edge\/(\d+)/)
        if(tem!=null)   {return {name:'Opera', version:tem[1]};}
        }
    M=M[2]? [M[1], M[2]]: [navigator.appName, navigator.appVersion, '-?'];
    if((tem=ua.match(/version\/(\d+)/i))!=null) {M.splice(1,1,tem[1]);}
    return {
      name: M[0],
      version: M[1]
    };
 }

var browser=get_browser();

if (!md.mobile() && !md.tablet()) {

  console.log('Device is computer')

  // images

  // scale perspective
  document.getElementById('scale_vertical').style.display = 'none';
  document.getElementById('scale_large').style.display = 'block';

  //shoes
  document.getElementById('shoes_vertical').style.display = 'none';
  document.getElementById('shoes').style.display = 'block';

  //neurons
  document.getElementById('neurons_vertical').style.display = 'none';
  document.getElementById('neurons').style.display = 'block';

  //lsd schematic
  document.getElementById('lsd_schematic_vertical').style.display = 'none';
  document.getElementById('lsd_schematic').style.display = 'block';

  //lsd components
  document.getElementById('lsd_components_vertical').style.display = 'none';
  document.getElementById('lsd_components_caption').style.display = 'none';

  //lsd mesh
  document.getElementById('3d_lsds_mesh_vertical').style.display = 'none';
  document.getElementById('3d_lsds_mesh').style.display = 'block';

  //gt vs pred
  document.getElementById('gt_vs_pred_lsds').style.display = 'none';
  document.getElementById('gt_vs_pred_lsds_caption').style.display = 'none';

  //zfinch
  document.getElementById('zfinch_dataset_vertical').style.display = 'none';
  document.getElementById('zfinch_dataset').style.display = 'block';

  //hemi
  document.getElementById('hemi_dataset_vertical').style.display = 'none';
  document.getElementById('hemi_caption_vertical').style.display = 'none';
  document.getElementById('hemi_dataset').style.display = 'block';

  //fib25
  document.getElementById('fib25_dataset_vertical').style.display = 'none';
  document.getElementById('fib25_dataset').style.display = 'block';

  //voi_mcm
  document.getElementById('voi_mcm_vertical').style.display = 'none';
  document.getElementById('voi_mcm').style.display = 'block';

  //hemi_voi
  document.getElementById('hemi_voi_vertical').style.display = 'none';
  document.getElementById('hemi_voi').style.display = 'block';

  //fib25_voi
  document.getElementById('fib25_voi_vertical').style.display = 'none';
  document.getElementById('fib25_voi').style.display = 'block';

  // watershed & agglom
  document.getElementById('watershed_separate_medium').style.display = 'none';
  document.getElementById('watershed_joined_medium').style.display = 'none';
  document.getElementById('agglom_joined_medium').style.display = 'none';
  document.getElementById('watershed_separate_large').style.display = 'block';
  document.getElementById('watershed_joined_large').style.display = 'block';
  document.getElementById('agglom_joined_large').style.display = 'block';

  // neuroglancer

  if (browser.name == 'Chrome' && browser.version >= 51){
    console.log('browser is chrome and version is >= than 51')
  }
  else if (browser.name == 'Firefox' && browser.version >= 46){
    console.log('browser is firefox and >= than 46')
  }
  else {
    console.log(browser)

    document.getElementById('fafb_div').style.display = 'none';
    document.getElementById('labels_div').style.display = 'none';
    document.getElementById('gt_lsds_div').style.display = 'none';
    document.getElementById('gt_vs_pred_div').style.display = 'none';
    document.getElementById('zfinch_div').style.display = 'none';
    document.getElementById('hemi_div').style.display = 'none';
    document.getElementById('fib25_div').style.display = 'none';
  }
}

else {

  console.log('Device is not computer')

  //images

  //scale perspective
  document.getElementById('scale_large').style.display = 'none';
  document.getElementById('scale_vertical').style.display = 'block';

  //shoes
  document.getElementById('shoes').style.display = 'none';
  document.getElementById('shoes_vertical').style.display = 'block';

  //neurons
  document.getElementById('neurons').style.display = 'none';
  document.getElementById('neurons_vertical').style.display = 'block';

  //lsd schematic
  document.getElementById('lsd_schematic').style.display = 'none';
  document.getElementById('lsd_schematic_vertical').style.display = 'block';

  //lsd components
  document.getElementById('lsd_components_vertical').style.display = 'block';

  //lsd mesh
  document.getElementById('3d_lsds_mesh').style.display = 'none';
  document.getElementById('3d_lsds_mesh_vertical').style.display = 'block';

  //gt vs pred
  document.getElementById('gt_vs_pred_lsds').style.display = 'block';

  //zfinch
  document.getElementById('zfinch_dataset').style.display = 'none';
  document.getElementById('zfinch_dataset_vertical').style.display = 'block';

  //hemi
  document.getElementById('hemi_dataset').style.display = 'none';
  document.getElementById('hemi_caption').style.display = 'none';
  document.getElementById('hemi_dataset_vertical').style.display = 'block';

  //fib25
  document.getElementById('fib25_dataset').style.display = 'none';
  document.getElementById('fib25_dataset_vertical').style.display = 'block';

  //voi_mcm
  document.getElementById('voi_mcm').style.display = 'none';
  document.getElementById('voi_mcm_vertical').style.display = 'block';

  //hemi_voi
  document.getElementById('hemi_voi').style.display = 'none';
  document.getElementById('hemi_voi_vertical').style.display = 'block';

  //fib25_voi
  document.getElementById('fib25_voi').style.display = 'none';
  document.getElementById('fib25_voi_vertical').style.display = 'block';

  // watershed / agglom
  document.getElementById('watershed_separate_large').style.display = 'none';
  document.getElementById('watershed_joined_large').style.display = 'none';
  document.getElementById('agglom_joined_large').style.display = 'none';
  document.getElementById('watershed_separate_medium').style.display = 'block';
  document.getElementById('watershed_joined_medium').style.display = 'block';
  document.getElementById('agglom_joined_medium').style.display = 'block';

  // neuroglancer

  document.getElementById('fafb_div').style.display = 'none';
  document.getElementById('labels_div').style.display = 'none';
  document.getElementById('gt_lsds_div').style.display = 'none';
  document.getElementById('gt_vs_pred_div').style.display = 'none';
  document.getElementById('zfinch_div').style.display = 'none';
  document.getElementById('hemi_div').style.display = 'none';
  document.getElementById('fib25_div').style.display = 'none';

}

</script>
