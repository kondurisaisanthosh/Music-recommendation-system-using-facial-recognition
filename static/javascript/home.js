Webcam.set({
    width:1000,
    height:565,
    image_format:'jpeg',
    jpeg_quality:90
})
Webcam.attach("#camera");
     function take_snapshot(){
        Webcam.snap(function(data_uri){
            console.log(data_uri)
            var base64data=data_uri.split(",")[1];
            console.log(base64data);
            var newbase64img=base64data.replace(/\//g,"SLASH");
//            console.log("2========"+newbase64img);
            const options={
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify(newbase64img)
            }
            fetch('/imagecapture/'+newbase64img)
                .then(response => response.json())
                .then(data => console.log(data));
        });
    }
function retake(){
    window.location.reload();
}