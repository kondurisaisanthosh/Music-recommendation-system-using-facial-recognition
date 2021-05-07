Webcam.set({
    width:750,
    height:423,
    image_format:'jpeg',
    jpeg_quality:90
})
let playlists = new Map();
playlists.set("happy","https://open.spotify.com/embed/playlist/5MPIVMVxSdXXXiwBQM6a45");
playlists.set("sad","https://open.spotify.com/embed/playlist/3NErR0TbvorTmM65GptZlP");
playlists.set("surprise","https://open.spotify.com/embed/playlist/6hMG5j7zDiSZij7NDIfDdW");
playlists.set("neutral","https://open.spotify.com/embed/playlist/5kXFRi7s7it02gge12kGra");
playlists.set("disgust","https://open.spotify.com/embed/playlist/4bSG6gA0zPVgiqKGStSkzV");
playlists.set("fear","https://open.spotify.com/embed/playlist/3ohYn6zM5RiqNPx4YVz3Re");
playlists.set("angry","https://open.spotify.com/embed/playlist/4SDCW3gQcNlD37XsM5ca6D");
playlists.set("NO VALUE","https://open.spotify.com/embed/playlist/5MPIVMVxSdXXXiwBQM6a45");
let playlist;

Webcam.attach("#camera");
function take_snapshot(){
    Webcam.snap(function(data_uri){
        document.getElementById('camera').innerHTML = '<img src="'+data_uri+'"/>';
        var base64data=data_uri.split(",")[1];
        var newbase64img=base64data.replace(/\//g,"SLASH");
        getEmotion(newbase64img).then(data=>{
                                playlist=playlists.get(data);
                                console.log(playlist);
                                document.getElementById("spotify").src=playlist;
                                document.getElementById("Mood").innerHTML="Person is "+data;
                            });
        });
}

async function getEmotion(newbase64img){
    try{
        const result=await fetch('/imagecapture/'+newbase64img);
        const data=await result.text();
        return data;
    }catch(error){
        console.log(error)
    }
}

function retake(){
    window.location.reload();
}
document.getElementById('myFileInput').addEventListener("change",function(){
    console.log("upload Initiated");
    const reader=new FileReader();
    reader.addEventListener("load",()=>{
        data_uri=reader.result;
        picture=document.getElementById('camera').innerHTML = '<img width="750" height="423" src="'+data_uri+'"/>';


        var base64data=data_uri.split(",")[1];
        var newbase64img=base64data.replace(/\//g,"SLASH");
        getEmotion(newbase64img).then(data=>{
            playlist=playlists.get(data);
            document.getElementById("spotify").src=playlist;
            document.getElementById("Mood").innerHTML="Person is "+data;
        });
    });
    reader.readAsDataURL(this.files[0]);
 });