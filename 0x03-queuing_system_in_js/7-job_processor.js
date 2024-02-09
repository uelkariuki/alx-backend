const kue = require('kue');
const queue = kue.createQueue();

let blacklisted_numbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklisted_numbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
  }
}

queue.process(`push_notification_code_2`, 2, function (job, done) {
  const phoneNumber = job.data.phoneNumber;
  const message = job.data.message;

  sendNotification(phoneNumber, message, job, done);
});
