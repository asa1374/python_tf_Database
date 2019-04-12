var compo = compo || {}
compo = {
    input_form : e=>{
        return "'<section>'\n" +
            "+'  <h3 class=\"h3 text-center mb-5\">배추 가격 예측하기</h3>'\n" +
            "+'  <div class=\"row wow fadeIn\">'\n" +
            "+'    <div class=\"col-lg-6 col-md-12 px-4\">'\n" +
            "+'      <form action=\"/\" method=\"post\">'\n" +
            "+'        <div class=\"form-group\">'\n" +
            "+'          <label for=\"formGroupExampleInput\">평균 온도</label>'\n" +
            "+'          <input type=\"text\" name=\"avg_temp\" class=\"form-control\" placeholder=\"평균 온도를 입력하세요.\">'\n" +
            "+'        </div>'\n" +
            "+'        <div class=\"form-group\">'\n" +
            "+'          <label for=\"formGroupExampleInput\">최소 온도</label>'\n" +
            "+'          <input type=\"text\" name=\"min_temp\" class=\"form-control\" placeholder=\"최소 온도를 입력하세요.\">'\n" +
            "+'        </div>'\n" +
            "+'        <div class=\"form-group\">'\n" +
            "+'          <label for=\"formGroupExampleInput\">최대 온도</label>'\n" +
            "+'          <input type=\"text\" name=\"max_temp\" class=\"form-control\" placeholder=\"최대 온도를 입력하세요.\">'\n" +
            "+'        </div>'\n" +
            "+'        <div class=\"form-group\">'\n" +
            "+'          <label for=\"formGroupExampleInput\">강수량</label>'\n" +
            "+'          <input type=\"text\" name=\"rain_fall\" class=\"form-control\" placeholder=\"강수량을 입력하세요.\">'\n" +
            "+'        </div>'\n" +
            "+'        <button type=\"submit\" class=\"btn btn-primary btn-md pull-right\">예측하기</button>'\n" +
            "+'      </form>'\n" +
            "+'    </div>'\n" +
            "+'    <div class=\"col-lg-6 col-md-12\">'\n" +
            "+'      {% if price %}'\n" +
            "+'        <h5 class=\"text-center mt-3\">결과: {{ price }}</h5>'\n" +
            "+'      {% endif %}'\n" +
            "+'    </div>'\n" +
            "+'  </div>'\n" +
            "+'</section>'"
    }
};