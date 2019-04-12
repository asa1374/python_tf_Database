$(document).ready(()=>{
    main.init();
    main.onCreate();
});

var main = main || {}
main = (e=>{
    let avg_temp,min_temp,max_temp,rain_fall;

    let init = e =>{
        avg_temp = $('#avg_temp');
        min_temp = $('#min_temp');
        max_temp = $('#max_temp');
        rain_fall = $('#rain_fall');
    };
    let onCreate = e=>{
        setContentView();
    };
    let setContentView = e=>{
        $('#result_btn').click(e=>{
            e.preventDefault();
        alert('평균은 ' + avg_temp.val() +
            min_temp.val() + max_temp.val() + rain_fall.val())
           /* $.getJSON($SCRIPT_ROOT+'/calc',x,d=>{
                    if (d.result.toString().length>13){
                        digitError();
                    } else{
                        alert(d.result)
                    }
                });*/
            })
    };
    let cleardata= ()=>{
        avg_temp.val('');
        min_temp.val('');
        max_temp.val('');
        rain_fall.val('');
    };
    return {init : init,onCreate : onCreate}
})();