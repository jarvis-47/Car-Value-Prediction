function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var dist = document.getElementById("uiDist");
    var year = document.getElementById("uiYear");
    var brand = document.getElementById("uiBrand");
    var model = document.getElementById("uiModel");
    var fuel = document.getElementById("uiFuel");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    var url = "http://127.0.0.1:5000/predict_car_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        dist: parseFloat(dist.value),
        model_year: parseFloat(year.value),
        brand: brand.value,
        model: model.value,
        fuel_type: fuel.value
    },function(data, status) {
        console.log(data.estimated_car_price);
        estPrice.innerHTML = "<h2>" + data.estimated_car_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "brands loaded" );
    var url = "http://127.0.0.1:5000/get_brand_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_brand_names request");
        if(data) {
            var brand = data.brands;
            var uiBrand = document.getElementById("uiBrand");
            $('#uiBrand').empty();
            for(var i in brand) {
                var opt = new Option(brand[i]);
                $('#uiBrand').append(opt);
            }
        }
    });

    console.log( "models loaded" );
    var url = "http://127.0.0.1:5000/get_model_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_model_names request");
        if(data) {
            var model = data.models;
            var uiModel = document.getElementById("uiModel");
            $('#uiModel').empty();
            for(var i in model) {
                var opt = new Option(model[i]);
                $('#uiModel').append(opt);
            }
        }
    });

    console.log( "fuel_type loaded" );
    var url = "http://127.0.0.1:5000/get_fuel_types"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_fuel_types request");
        if(data) {
            var fuel_type = data.fuel_types;
            var uiFuel = document.getElementById("uiFuel");
            $('#uiFuel').empty();
            for(var i in fuel_type) {
                var opt = new Option(fuel_type[i]);
                $('#uiFuel').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;