import { createClient, print } from 'redis';
const client = createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
