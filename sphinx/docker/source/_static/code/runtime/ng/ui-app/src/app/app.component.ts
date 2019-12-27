import { Component, OnInit } from '@angular/core';
import { environment } from './../environments/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  production = false;
  apiKey = 'NOT SET';
  serviceUrl = 'NOT SET';

  constructor() {
    this.production = environment.production;
    this.apiKey = environment.apiKey;
    this.serviceUrl = environment.serviceUrl;
  }

  ngOnInit(): void {
    console.log(`production = {this.production}`);
    console.log(`apiKey = {this.apiKey}`);
    console.log(`serviceUrl = {this.serviceUrl}`);
  }
}
