Webcam.set({
    width:1000,
    height:565,
    image_format:'jpeg',
    jpeg_quality:90
})
Webcam.attach("#camera");
    function take_snapshot(){
        Webcam.snap(function(data_uri){
            document.getElementById('camera').innerHTML = '<img src="'+data_uri+'"/>';
    });
}
function retake(){
    window.location.reload();
}