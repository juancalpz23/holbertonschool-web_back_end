import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  // Before each test, create a new queue in test mode
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode = true; // Enable test mode to track jobs without processing them
  });

  // After each test, clear the queue and exit test mode
  afterEach(() => {
    queue.testMode = false;
    queue.shutdown(500, (err) => {
      if (err) console.error('Error shutting down queue:', err);
    });
  });

  it('should display an error message if jobs is not an array', () => {
    try {
      createPushNotificationsJobs('not an array', queue);
    } catch (err) {
      expect(err.message).to.equal('Jobs is not an array');
    }
  });

  it('should create two new jobs in the queue', (done) => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 5678 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Use queue.testMode to check if the jobs are added to the queue
    queue.process('push_notification_code_3', (job, done) => {
      done();
    });

    // Check if two jobs were created
    queue.on('job enqueue', (id, type) => {
      if (type === 'push_notification_code_3') {
        const job = queue.getJob(id);
        job.getData((err, data) => {
          expect(data).to.include({ phoneNumber: '4153518780' });
        });
      }
    });

    setTimeout(() => {
      // Ensure two jobs were created in the queue
      expect(queue.jobs.length).to.equal(2);
      done();
    }, 100);
  });
});
