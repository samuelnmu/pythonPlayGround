let input = document.querySelector("input");
input.addEventListener("input", async function(){
    let response = await fetch("serch?q=" + input.value);
    let shows = await response.text();
    document.querySelector("ul").innerHTML = shows;
})