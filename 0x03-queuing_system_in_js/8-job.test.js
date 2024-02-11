const kue = require('kue');
const chai = require('chai');
const expect = chai.expect;
const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs', function () {
  let queue;

  beforeEach(function () {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.exit();
    queue.testMode.clear();
  });

  it('should create jobs in the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518785',
        message: 'This is the code 2234 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    for (let i = 0; i < jobs.length; i++) {
      expect(queue.testMode.jobs[i].type).to.equal('push_notification_code_3');
      expect(queue.testMode.jobs[i].data).to.deep.equal(jobs[i]);
    }
  });

  it('should throw an error if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
      'Jobs is not an array'
    );
  });
});
