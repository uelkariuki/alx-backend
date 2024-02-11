const kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (let job of jobs) {
    const newJob = queue
      .create('push_notification_code_3', job)
	  newJob
		.on('complete', function (result) {
		  console.log(`Notification job ${newJob.id} completed`);
		})
		.on('failed', function (errorMessage) {
		  console.log(`Notification job #${newJob.id} failed: ${errorMessage}`);
		})
		.on('progress', function (progress, data) {
		  console.log(`Notification job #${newJob.id} ${progress}% complete`);
		});
      newJob.save(function (err) {
        if (!err) {
          console.log(`Notification job created: ${newJob.id}`);
        }
      });
  }
}

module.exports = createPushNotificationsJobs;
