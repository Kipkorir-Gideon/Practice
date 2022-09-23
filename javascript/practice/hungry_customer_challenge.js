var bun = true;
var patty = true;
var cheese = true;
var veggie = true;
var mayonnaisse = true;
var ketchup = true;
 var order = bun && patty && veggie &&(ketchup || mayonnaise);
 var happyCustomer = order;
 console.log(happyCustomer);

 var secondOrder = bun && patty && cheese && mayonnaisse && !veggie;
 happyCustomer = secondOrder;
 console.log(happyCustomer);