import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Doc, NawahService } from 'ng-nawah';

@Component({
	selector: 'app-admin-dashboard',
	templateUrl: './admin-dashboard.component.html',
	styleUrls: ['./admin-dashboard.component.css']
})
export class AdminDashboardComponent implements OnInit {

	get user(): Doc {
		return this.nawah.session?.user;
	}

	constructor(private nawah: NawahService, private router: Router) { }

	ngOnInit(): void {
	}

	signout(): void {
		this.nawah.signout().subscribe({
			next: (res) => {
				this.router.navigate(['/admin']);
			}
		})
	}

}
