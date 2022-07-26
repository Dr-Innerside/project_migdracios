// 1. getElementById
console.log("getElementById");
const card_input = document.getElementById("card_input");
console.log(card_input);
const message1 = card_input.value;
const message2 = card_input.innerText;
console.log(message1, message2);

// 2. getElementsByClassName
const card_button_object = document.getElementsByClassName("card_button");
console.log(card_button_object);
const card_button_element = document.getElementsByClassName("card_button")[0];
console.log(card_button_element);
console.log(card_button_element.value);

// 3. childNodes
const card_box = document.getElementById("card_box");
const first_child = card_box.childNodes[0];
const second_child = card_box.childNodes[1];
console.log(first_child);
console.log(second_child);

// 4. parentElement
const card_input2 = document.getElementById("card_input");
const parent_element = card_input2.parentElement;
const ancestor_element = card_input2.parentElement.parentElement;
console.log(parent_element);
console.log(ancestor_element);
console.log(parent_element.parentElement);

// 5. createElement
const card_h3 = document.createElement("h3");
console.log(card_h3);

// 6. appendChild
card_box.appendChild(card_h3);
console.log(card_h3);
console.log("개발자 도구의 Element(요소)를 열어 HTML을 확인해보세요!");