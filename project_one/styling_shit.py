
def display_bad_reviewes(list_bad_reviewes):
    res=''''''
    for i in list_bad_reviewes:
        res+='''<div class="alert alert-danger alert-dismissible">
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    <strong>bad review!</strong>'''+i+'''
  </div>'''
        
    return res


def style(good,bad,list_bad_reviewes):
    return """
    <head>
    <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
  
  
  </head>
    
    
    <h2 class="neonText">positive reviews</h2> 
    <center>
    <div class="half-arc" style="--percentage:"""+str(int(good*100))+"""%;">
  <span class="label">"""+str(round(good*100,2))+"""%</span>
</div></center></br>

<center>
<h2 class="neonText">negitive reviews</h2> 
<div class="half-arc" style="--percentage:"""+str(int(bad*100))+"""%;">
  <span class="label">"""+str(round(bad*100,2))+"""%</span>
</div></center> <br><br>"""+progress_stye+'''<h1 class="neonText">critical review: </h1><br>'''+display_bad_reviewes(list_bad_reviewes)
progress_stye='''
          
          <style>
          .neonText {
  color: #fff;
  text-shadow:
      0 0 7px #fff,
      0 0 10px #fff,
      0 0 21px #fff,
      0 0 42px #0fa,
      0 0 82px #0fa,
      0 0 92px #0fa,
      0 0 102px #0fa,
      0 0 151px #0fa;
}

/* Additional styling */
  
body {
  font-size: 18px;
  font-family: "Vibur", sans-serif;
  background-color: #010a01;
}  

h1, h2 {
  text-align: center;
  text-transform: uppercase;
  font-weight: 400;
}
  

.container {
  margin-top: 20vh;
}
            html, body {
    <!--display: flex;-->
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    gap: 40px;
}

.half-arc {
    position: relative;
    width: 200px;
    height: 100px;
    border-top-left-radius: 120px;
    border-top-right-radius: 120px;
    border-bottom: 0;
    background: #d9d9d9;
    box-sizing: border-box;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.half-arc:before {
    content: "";
    position: absolute;
    display: block;
    top: 0;
    left: 0;
    width: 100%;
    height: 200%;
    border-radius: 50%;
    background-image: conic-gradient(#9c27b0, #3f51b5 calc(var(--percentage, 0) / 2), #bbb 0);
    transition: transform .5s ease-in-out;
    z-index: 1;
    transform: rotate(270deg);
}

.half-arc:after {
    content: "";
    position: absolute;
    display: block;
    background: #dddddd;
    z-index: 2;
    width: calc(100% - 32px);
    height: calc(200% - 32px);
    border-radius: 50%;
    top: 16px;
    left: 16px;
}

.half-arc span {
    color: #673ab7;
    z-index: 3;
    text-align: center;
}
          </style>'''