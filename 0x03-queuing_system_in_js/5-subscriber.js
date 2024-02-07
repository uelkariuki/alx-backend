import { createClient, print } from 'redis';
const client = createClient();
const subscriber = client.duplicate();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err}`)
);

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(channel);
    process.exit();
  }
});
