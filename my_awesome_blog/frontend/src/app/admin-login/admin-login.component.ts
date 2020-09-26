import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Doc, NawahService, Res } from 'ng-nawah';

@Component({
	selector: 'app-admin-login',
	templateUrl: './admin-login.component.html',
	styleUrls: ['./admin-login.component.css']
})
export class AdminLoginComponent {

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
