#!/usr/bin/node
if (process.arg.length === 0) {
	console.log('No argument');
}
else if (process.arg.length === 1) {
	console.log('Argument found');
}
else {
	console.log('Arguments found');
}
