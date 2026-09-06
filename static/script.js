const form = document.getElementById("ticketForm");

form.addEventListener("submit", function(event) {

    const name = document.getElementById("name").value;
    const title = document.getElementById("title").value;

    console.log("Sending ticket to Flask...");
    console.log("Name:", name);
    console.log("Title:", title);

});