import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {ApiService} from "../api/service";
import {ActivatedRoute, Router} from "@angular/router";
import {PersonCreate} from "../api/model";

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {

  formGroup: FormGroup;
  created = false;

  constructor(private api: ApiService, private router: Router, private route: ActivatedRoute, private fb: FormBuilder) {
    this.formGroup = fb.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      gender: ['', Validators.required],
      age: ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.formGroup.status === 'VALID') {
      const p = new PersonCreate(
        this.formGroup.value.firstName,
        this.formGroup.value.lastName,
        this.formGroup.value.gender,
        this.formGroup.value.age
      );

      this.api.createPerson(p)
        .subscribe(
          r => {
            console.log(r);
            this.formGroup.reset();
            this.created = true;
          },
          e => console.error(e)
        );
    }
  }

  cancelCreate(): void {
    this.router.navigate(['/default']);
  }

}
