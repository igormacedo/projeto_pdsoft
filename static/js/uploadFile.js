
$(function() {
    // We can attach the `fileselect` event to all file inputs on the page
    $(document).on('change', ':file', function() {
        var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [numFiles, label]);
    });

    // We can watch for our custom `fileselect` event like this
    $(document).ready( function() {
        $(':file').on('fileselect', function(event, numFiles, label) {

            var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;

            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }

            readURL(this);
        });

        $('#btn_save').on('click', function(){
            if( document.getElementById("cd_login").value != "" &&
                document.getElementById("cd_email").value != "" &&
                document.getElementById("cd_nome").value != "" &&
                document.getElementById("cd_senha").value != "" &&
                document.getElementById("cd_foto").value != "")
            {
                document.getElementById("user_form").submit();
            }
            else{
                alert("Campos obrigatórios não foram preenchidos corretamente");
            }
        });
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#profile_pic').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
});
