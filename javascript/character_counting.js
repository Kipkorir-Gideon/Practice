var tweet = prompt("Compose your tweet:");
var tweetCount = tweet.length;
var tweetUnder140 = tweet.slice(0,140);
alert("You have written " + tweetCount + " characters, you have " + (140 - tweetCount) + " characters remaining.");
alert(tweetUnder140);