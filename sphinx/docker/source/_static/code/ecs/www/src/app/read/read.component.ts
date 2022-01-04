import { Component, OnInit } from '@angular/core';
import {Person} from "../api/model";
import {ApiService} from "../api/service";
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit {

  people: Array<Person>;
  skip = 0;
  limit = 10;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute) {
    this.people = [];
  }

  ngOnInit(): void {
    this.api.getPeople(this.skip, this.limit)
      .subscribe(
        r => this.people = r,
        e => console.error(e)
      );
  }

  updateClicked(personId: number): void {
    this.router.navigate(['/update'], {queryParams: { personId }});
  }

  deleteClicked(personId: number): void {
    this.router.navigate(['/delete'], {queryParams: { personId }})
  }

  nextClicked(): void {
    const skip = this.skip + this.limit;
    this.api.getPeople(skip, this.limit)
      .subscribe(
        r => {
          if (r.length > 0) {
            this.people = r;
            this.skip = skip;
          }
        },
        e => console.error(e)
      );
  }

  prevClicked(): void {
    const skip = this.skip - this.limit;
    if (skip >= 0) {
      this.skip = skip;

      this.api.getPeople(this.skip, this.limit)
        .subscribe(
          r => this.people = r,
          e => console.error(e)
        );
    }
  }

}
