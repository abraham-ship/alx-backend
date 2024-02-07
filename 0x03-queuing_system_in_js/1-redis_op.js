import redis from 'redis';

// create redis client
const client = redis.createClient();

// connect to redis server
client.on('connect', () => console.log('Redis client connected to the server'));

// handle connection errors
client.on('error', (err) => console.error(`Redis client not connected to the server: Error: ${err.message}`));

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, val) => {
		if (err) {
			console.log(err)
		}
		else {
			console.log(val)}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
