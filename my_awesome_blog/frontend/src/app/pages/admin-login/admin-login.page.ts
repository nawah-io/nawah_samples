import { Component } from '@angular/core';
import { Router } from '@angular/router';

import { NawahService, Res, Doc } from 'ng-nawah';


@Component({
  selector: 'page-admin-login',
  templateUrl: 'admin-login.page.html',
  styleUrls: ['admin-login.page.css']
})
export class AdminLoginPage {

  email: string = '';
  password: string = '';

  constructor(private nawah: NawahService, private router: Router) { }

  auth() {
    try {
      this.nawah.auth('email', this.email, this.password).subscribe({
        next: (res) => {
          alert('Authenticated!');
          this.router.navigate(['/admin', 'dashboard']);
        },
        error: (res: Res<Doc>) => {
          alert(res.msg || res);
        },
      });
    } catch (err) {
      alert(err);
    }
  }

}