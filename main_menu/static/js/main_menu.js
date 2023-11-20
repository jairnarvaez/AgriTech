const getOptionChart_humidity = async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_humidity/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");
    }
};

const getOptionChart_nutrients = async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_nutrients/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");

    }
};

const getOptionChart_temperature= async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_temperature/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");

    }
};

const getOptionChart_phosphorus = async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_phosphorus/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");

    }
};

const getOptionChart_pie = async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_pie/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");

    }
};

const getOptionChart_large = async () => {
    try {
        const response = await fetch("http://146.190.51.184:8000/get_graph_large/");
        return await response.json();
    } catch (ex) {
        console.log("error de red");

    }
};

const initChart = async () => {
    const myChart_humidity = echarts.init(document.getElementById("graph_humidity"));
    const myChart_nutrients = echarts.init(document.getElementById("graph_nutrients"));
    const myChart_temperature = echarts.init(document.getElementById("graph_temperature"));
    const myChart_phosphorus= echarts.init(document.getElementById("graph_phosphorus"));
    const myChart_pie= echarts.init(document.getElementById("graph_pie"));
    const myChart_large= echarts.init(document.getElementById("graph_large"));


    myChart_humidity.setOption(await getOptionChart_humidity());
    myChart_nutrients.setOption(await getOptionChart_nutrients());
    myChart_temperature.setOption(await getOptionChart_temperature());
    myChart_phosphorus.setOption(await getOptionChart_phosphorus());
    myChart_pie.setOption(await getOptionChart_pie());
    myChart_large.setOption(await getOptionChart_large());

};

window.addEventListener("load", async () => {
    await initChart();
    await initChart();
    const myChart_humidity = echarts.init(document.getElementById("graph_humidity"));
    const myChart_nutrients = echarts.init(document.getElementById("graph_nutrients"));
    const myChart_temperature = echarts.init(document.getElementById("graph_temperature"));
    const myChart_phosphorus= echarts.init(document.getElementById("graph_phosphorus"));
    const myChart_pie= echarts.init(document.getElementById("graph_pie"));
    const myChart_large= echarts.init(document.getElementById("graph_large"));



    setInterval(async () => {
        await initChart();
    }, 30000);

    setInterval(async () => {
        myChart_humidity.resize();
        myChart_nutrients.resize();
        myChart_temperature.resize();
        myChart_phosphorus.resize();
        myChart_pie.resize();
        myChart_large.resize();

    }, 1000);

    

});
