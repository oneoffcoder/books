import { Component, OnInit } from '@angular/core';
import {ApiService} from "../api/service";
import {ActivatedRoute, Router} from "@angular/router";
import {Person} from "../api/model";
import {filter, map, mergeMap} from "rxjs/operators";

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit {

  person?: Person;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute) {
    this.person = undefined;
  }

  ngOnInit(): void {
    this.route.queryParams.pipe(
      filter(p => p['personId']),
      map(p => p['personId']),
      mergeMap(id => this.api.getPersonById(id))
    ).subscribe(
      p => this.person = p,
      e => {
        this.person = undefined;
        console.error(e);
      }
    );
  }

}
