<!doctype html>
% from bottle import url
<html>

</html>
<body>
<link rel="stylesheet" href="{{ url('static', filepath='css/bootstrap.min.css') }}">

<form method="post">
  <div class="form-group row">
    <label class="col-4 col-form-label" for="titulo">{{ form.titulo.label }}</label>
    <div class="col-8">
      {{ !form.titulo(class_="form-control", required="required") }}
    </div>
  </div>
  <div class="form-group row">
    <label for="texto" class="col-4 col-form-label">Texto</label>
    <div class="col-8">
      {{ !form.texto(class_="form-control", required="required") }}
    </div>
  </div>
  <div class="form-group row">
    <div class="offset-4 col-8">
      <button name="submit" type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</form>
</body>