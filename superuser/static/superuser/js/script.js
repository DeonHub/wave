
const getLogo = () => {

    const logo = document.getElementById('logo');
    const logoPreview = document.getElementById('logo-preview');
    const previewImage = document.querySelector(".logo-image");
    const previewTextDefault = document.querySelector(".logo-text");

    logo.addEventListener('change', function() {
            const file = this.files[0];
            
            if (file){

                    const reader = new FileReader()

                    previewTextDefault.style.display = "none"
                    previewImage.style.display = "block"
                    logoPreview.style.border = "none"

                    reader.addEventListener('load', function() {
                            console.log(this.result)
                            previewImage.setAttribute("src", this.result)  
                    });

                    reader.readAsDataURL(file);

            }else{
                    previewTextDefault.style.display = null
                    previewImage.style.display = null   
                    logoPreview.style.border = null
                    previewImage.setAttribute("src", "") 
            }
    })
}


const getVideo = () => {
        const video = document.getElementById('video-file');
        const videoPreview = document.getElementById('video-preview');
        const videoPlayer = document.querySelector('.video-player');
        // const previewTextDefault = document.querySelector('.video-text');
    
        video.addEventListener('change', function() {
            const file = this.files[0];
    
            if (file) {
                const reader = new FileReader();
    
                // previewTextDefault.style.display = 'none';
                videoPlayer.style.display = 'block';
                videoPreview.style.border = 'none';
    
                reader.addEventListener('load', function() {
                    videoPlayer.setAttribute('src', this.result);
                });
    
                reader.readAsDataURL(file);
            } else {
                // previewTextDefault.style.display = null;
                videoPlayer.style.display = null;
                videoPreview.style.border = null;
                videoPlayer.setAttribute('src', '');
            }
        });
    };
    


const displayContent = (event) => {
        const banner_content = document.getElementById('banner_content')

        if(event.checked == false){
                banner_content.style.display = "none";
        }
        else{
                banner_content.style.display = "block";
        }
        
}
