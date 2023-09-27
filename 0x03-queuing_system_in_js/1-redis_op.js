//Connects to the Redis server running on my machine
import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (error, reply) => {
    if (error) {
      console.log(error.message);
    }
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
