$(document).ready(function () {
    
  // Functions to add and remove fields in movie_form.html
  function addInput(event) {
    $(`#${event.data.targetId}`).append(
      `<div class="col s6 ${event.data.newClass}"><input name="${event.data.name}[]" type="text" placeholder="${event.data.placeholder}" class="validate" required></div>`
    );
  }
  function removeInput(event) {
    $(`.${event.data.class}:last`).remove();
  }

  //Form add or subtract input button triggers
  $("#actor_add").click(
    {
      targetId: "movie_actors",
      newClass: "actor-input",
      name: "actors",
      placeholder: "Name...",
    },
    addInput
  );

  $("#actor_remove").click({ class: "actor-input" }, removeInput);

  $("#director_add").click(
    {
      targetId: "movie_directors",
      newClass: "director-input",
      name: "directors",
      placeholder: "Name...",
    },
    addInput
  );

  $("#director_remove").click({ class: "director-input" }, removeInput);

  $("#language_add").click(
    {
      targetId: "movie_languages",
      newClass: "language-input",
      name: "languages",
      placeholder: "Add language",
    },
    addInput
  );

  $("#language_remove").click({ class: "language-input" }, removeInput);
});
