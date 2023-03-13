#!/usr/bin/node
if (process.argv.length < 1) {
	console.log('No argument');
}
else if (process.argv.length === 1) {
	console.log('Argument found');
}
else (process.argv.length > 1) {
	console.log('Arguments found');
}
