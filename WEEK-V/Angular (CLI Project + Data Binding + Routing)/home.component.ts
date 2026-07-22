import { Component } from '@angular/core';

@Component({
  selector: 'app-home',
  template: `
    <section>
      <h2>Welcome, Student!</h2>
      <p>Today's event: Coding Club meetup at 4:00 PM.</p>
      <button (click)="count = count + 1">RSVP</button>
      <p>RSVP count: {{ count }}</p>
    </section>
  `
})
export class HomeComponent {
  count = 0;
}
